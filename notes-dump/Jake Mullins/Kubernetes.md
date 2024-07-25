[Link](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
Kubernetes is pretty important, might as well learn it now

qa.com/self-paced-learning
github kelseyhightower kubernetes-the-hard-way
## Using Minikube to create a cluster
**Control Plane**: Coordinates the cluster. Coordinates scheduling, state, scaling, and new updates.
**Nodes**: Workers that run applications. Each node has a Kubelet, which is an agent that communicates with the control plane using the Kubernetes API.

Create a deployment:
```shell
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
```

# Architecture
Have a master machine:
- `etcd`: Configuration information for each node in the cluster. High availability key-value store. Accessible only by Kubernetes API Server.
- `API Server`: Central management point of the cluster. 
- `Controller Manager`: Daemon regulates the state of a cluster, sends state information to API. Does actions on cluster to try and match desired state. Has multiple child controllers including:
	- `Replication Controller`:
	- `Endpoint Controller`:
	- `Namespace Controller`:
	- `Service Account Controller`:
- `Scheduler`: Distributes workload amongst nodes in a cluster. Tracks utilization of workload.
Each worker node has the following components:
- `Docker runtime`: Or other OCI-compliant runtime.
- `Kubelet service`: Small service used to relay information to the control plan on the Master node. Interacts with `etcd`. Manages networking stuff like port forwarding.
- `Kubernetes Proxy Service`: Reverse proxy that forwards request to correct containers, as well as doing some limited load balancing. Does health checks.
Terms:
- `Nodes`: Worker machine that deploys pods.
- `Pods`: Smallest deployable unit in Kubernetes. Represents one or more containers. Containers within the same pod.
- `Namespaces`: Visibility scopes for resources.
- `ReplicaSets`: Guarantee that a set number of replicas will be running. Continuously monitoring the health of pods in a set.
- `Deployments`: Wrap `ReplicaSets` with support for declarative updates and rollbacks. Higher level.
- `Services`: Expose pods to netowkr.
- `Job`: Workloads that can be run arbitrarily on a cluster.
- `Volumes`: Mount external filesystem storage.
- `Secrets`: Inject sensitive data such as keys and certs.
- `ConfigMaps`: Simple non-sensitive YAML files.
- `DaemonSets`: Add global functionality to a cluster. Ensure all nodes run at least a copy of this pod.
![[Screenshot 2024-07-15 at 3.19.11 PM.png]]
![[Screenshot 2024-07-16 at 9.32.34 AM.png]]

`kube-proxy`: Daemon that runs on each node for proxying network traffic.
`kube-controller-manager`: Daemon that interfaces with the API server and makes changes to attempt to match the desired state.
`kube-scheduler`: Control plan process which assigns Pods to Nodes. Basically load balances based off of resource utilization rates.
# CTFs and Playgrounds
[Kubernetes Goat](https://madhuakula.com/kubernetes-goat/)
[Reddit thread on this subject](https://www.reddit.com/r/kubernetes/comments/1b9e62g/looking_for_a_k8s_ctf/)
[Lab4grabs.io](https://www.labs4grabs.io/)
# kubernetes-the-hard-way
Fixes:
Change the hostnames without `hostnamectl`, just use `docker-compose.yaml`
Found link for `encryption-config.yaml` [here](https://github.com/kelseyhightower/kubernetes-the-hard-way/issues/768)
