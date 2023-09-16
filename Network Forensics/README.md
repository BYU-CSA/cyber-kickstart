# Network Forensics  
Forensics is the art of investigating an environment to try and figure out what happened there in the past. Network forensics involves looking at the network traffic of a computer and piecing together what data they were sending and receiving. 

Typically in network forensics CTF problems you're working with packet capture files (.pcap or .pcapng). These files will contain all of the network packets sent and received from a certain NIC on a computer for a certain time, and they're generally created and viewed from a program similar to [Wireshark](https://www.wireshark.org/). 

This lesson assumes that you already have an understanding of the 7 OSI layers and the IP protocol. If you need a quick refresher on that you can go [here](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/). Knowing networking ports and protocols is also useful, and you can brush up on that [here](https://en.wikipedia.org/wiki/Port_(computer_networking)). 

## Common Tools

* [Wireshark](https://www.wireshark.org/)
    * Several packet capture tools exist, each with different specialties, but Wireshark is far and away the most popular (plus it's free). There are many different online tutorials on how to use Wireshark, so we won't go over the specifics in this lesson, but we'd encourage you to run through [this](https://www.freecodecamp.org/news/learn-wireshark-computer-networking/) before attempting the practice challenges. 

## Practice Challenges

```md
Should've used HTTPS (Unpublished)
--------
After some hard work you've managed to sniff some packets from a computer on a network you've been trying to pentest! And what luck, it looks like this person signed into their router using it's web portal. What password did they use to get in?

Refer to chall.pcapng

Writeup: This challenge was created just for this lesson. Message Dallin Kaufman on Slack if you think you've found it ;)
```

```md
Trivial Flag Transfer Protocol (Pico CTF 2021)
--------
Can you find the flag?

Refer to shark1.pcapng

Writeup: https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Forensics/Wireshark%20doo%20dooo%20do%20doo/Wireshark%20doo%20dooo%20do%20doo.md
```

```md
Yo, who's hacking me? (Unpublished)
--------
You've been keeping an eye on the network traffic going to and from your machine, and it looks like someone ran an nmap scan on you! What IP address did it?

Refer to chall.pcapng

Writeup: This challenge was created just for this lesson. Message Dallin Kaufman on Slack if you think you've found it ;)
```

## What's Next?

* [Pico CTF Forensics Challs](https://play.picoctf.org/practice?category=4&page=1)
    * Pico CTF is an awesome collection of beginner challenges ranked in order of difficulty. They have a pretty robust forensics section where you can sort through and find network forensics challenges to practice on!