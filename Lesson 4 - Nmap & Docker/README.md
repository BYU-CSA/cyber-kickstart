# Lesson 4 - Nmap and Docker
## Nmap
Like many tools in cybersecurity, Nmap is an open source tool that explores a network by scanning ports, services, and hosts by sending and receiving packets. The responses to those packets are then used to gather information on the target. 

Knowing how to use nmap is essential for any position in cybersecurity (especially pentesting) and is often used as a first step for CTF challenges. 

### Nmap in CTFs
* https://deskel.github.io/posts/thm/simple-ctf
* https://www.hackingarticles.in/hack-the-wintermute-1-ctf-challenge/
* https://www.secjuice.com/tryhackme-simple-ctf/

### Scan types
There's about a dozen images in the Nmap Photos folder that contain tons of different types of scans, but we'll cover the most commonly used and important ones below.

* `nmap ip_or_hostname` - this is the default non-sudo nmap scan. It performs a full TCP handshake with the 1000 most common ports after confirming the host is up by pinging.
    * `nmap -sT ip_or_hostname` is the same as the above command
    * A TCP handshake consist of 3 parts - the client reaches out and says "Hey I want to connect", the server responds and says "Are you sure?", and the client replies by saying "Yes I'm sure". Then, the handshake is complete and a connection is made. Most programs log connections after the TCP handshake is complete, so doing a full TCP handshake is **not** recommended to avoid detection better.
* `sudo nmap ip_or_hostname` - this is the default sudo nmap scan. It performs a SYN scan with the 1000 most common ports after confirming the host is up by pinging.
    * `sudo nmap -sS ip_or_hostname` is the same as the above command
    * This scan only performs a part of the TCP handshake. After the client reaches out, if it receives a response from the server, it marks the port as up but doesn't reply, preventing the handshake from being completed. Programs won't recognize this as a connection and won't log it. This is the preferred scan. 
* `sudo nmap -sV ip_or_hostname` - in the default scans, it only finds which ports are open and then tells you which services have historically been correlated with those ports. This scan goes a step further and sends additional probes to figure out which service exactly is listening on the port, including version numbers and sometimes OSes too.
* `sudo nmap -O ip_or_hostname` - this scan builds upon the default scan and also tries to guess the Operating System based on the minutiae of returning packets. 
    * Using the `-O --osscan-guess` option instead will print out OS guesses. In other words, if nmap can't determine with certainty the OS of the target, it will give you its best guess.
* `sudo nmap -A ip_or_hostname` - this is the "agressive" scan that does a SYN scan with service detection and OS guessing, plus some scripts.
* `sudo nmap -sn ip_or_hostname` - this does only a ping scan through ICMP echo requests and ARP packets. However, if ICMP echoing is disabled for a machine, this will fail.
* `sudo nmap -Pn ip_or_hostname` - in the event that a machine is not shown as up because ICMP echo is disabled, you can use this option to go ahead and do the scan anyway. Note that it will take a little bit longer.
* `sudo nmap -p ports ip_or_hostname` - you can specify exact ports to scan with this option
    * `-p 1`, `-p 80,53`, `-p 1-1500` are all valid ways of specifying one or multiple ports/port ranges
    * `-p-` and `-p '*'` means to scan all 65,535 TCP ports
* `sudo nmap -T4 ip_or_hostname` - this specifies the scan template. You can see a list of different templates and what they are [here](https://nmap.org/book/performance-timing-templates.html)

*Tip - pressing keys during a scan will print out a progress report*

### Examples
<img src="scan_example.png" width="700">

<img src="scan_example_2.png">

### Challenges
There's a site called [ScanMe.nmap.org](http://scanme.nmap.org/) that's designed to be scanned with Nmap. Take a crack at it and see what you find!

## Docker
Docker is a very popular containerization software that allows you to deploy pre-configured OSes in a lightweight environment. They are commonly used in CTFs, development, and the real world. Understanding how to load, deploy, and poke at a Docker container will be important to your future success. 

### Containers vs. Virtual Machines
While containers and virtual machines perform similar functions, they are fundamentally different by nature. The biggest difference that that virtual machines simulate virtual hardware (network card, hard drive, memory, etc.), while containers piggyback off of the hardware that the host OS is running on. They both have separate filesystems, but this is only at a software level. 

More specifics about containers and how they are different from VMs can be found [here](https://www.cybersecurity-insiders.com/containers-101-what-do-you-need-to-know/) and [here](https://www.weave.works/blog/a-practical-guide-to-choosing-between-docker-containers-and-vms). 

![Docker vs containers](containers-vs-virtual-machines.jpg)

### Common Commands
- `docker load <simple_ctf_docker_image.tar`
    - Loads a downloaded docker image
- `docker image ls`
    - Lists all loaded docker images on your machine
- `docker-compose up -d`
    - Starts a docker image based on a `docker-compose.yml` file
- `docker-compose down`
    - Stops a running docker image
- `docker run -it name_of_image /bin/bash`
    - Runs a bash shell *inside* a loaded but not running Docker container
- `docker ps -a`
    - Shows running/recently running images

### Challenge
We've created a custom Docker image for you, based on Alpine Linux, called `simple_ctf_docker_image.tar`. Use the commands above to load it, run `/bin/ash`, and find the `flag.txt` in the `/root/` directory!