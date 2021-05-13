# Lesson 1 - Introduction to CTFs
Welcome to our GitHub repo where we teach lessons about tools and methods used in Capture the Flag competitions! This is an online resource that you can access whenever you'd like. We plan on including scripts, links, tools, code, examples, and others to help you become more successful in CTFs! Our goal is to have multiple teams progress in our monthly CTF competitions that we participate in, and this is how we plan on doing it!

## Beginners Doc
Not sure what a CTF is or how it works? Don't worry, we've written up [a document](https://github.com/JustinApplegate/ctf-training/blob/main/Beginners.md) that can help answer some of the questions you may have about them. We won't take the time to answer all these questions in the first lesson because we want to dive right into it! Also in that beginner document is a list of basic skills that we're assuming (I know, so rude of us!) that you already have. If you aren't comfortable with those skills, we'll point you in the direction of some resources to learn them because they will be essential in using the tools and methods we'll teach. 

## Topics?
What do you want to learn? We've already included a list of [future topics](https://github.com/JustinApplegate/ctf-training/blob/main/Future_Topics.md) that we want to cover, but if there's something in particular you've been *dying* to learn, or something we don't have, let us know in Slack! 

We've also created a link to a survey where you can let us know what you want to learn: https://forms.gle/Gm2eaaCNFMrwqP239

# Technical Topics
## Linux
When it comes to cybersecurity and CTF competitions, having access to a Linux environment is at the very least super helpful, if not essential. There are several tools that have not been written for use in a Windows environment. So, what are your options??

* [Installing WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [Virtual machine](https://itsfoss.com/install-linux-in-virtualbox/)
* [Dual-boot](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/)

## LSB
This is a common steganography tool used to hide data (text, black+white photos, or color photos) in bits of an image. Look at the LSB Steganography.pptx file to learn about *HOW* LSB steg works. Then, look at some of the examples:

* [Before hiding data](https://raw.githubusercontent.com/JustinApplegate/ctf-training/main/Lesson%201%20-%20Introduction%20to%20CTFs/boston-skyline.png)
* [After hiding data](https://raw.githubusercontent.com/JustinApplegate/ctf-training/main/Lesson%201%20-%20Introduction%20to%20CTFs/txt-em-boston.png)

**Tools:**
* Website for text/black&white photo LSB - https://stegonline.georgeom.net/upload
* Website for color photo LSB - https://incoherency.co.uk/image-steganography/
* Python script for text LSB - https://github.com/djrobin17/image-stego-tool

**Notes:**
* LSB steganography is only used on PNG photos (not JPEGs) because JPEGS are a lossy photo format, meaning that when you compress then uncompress it, you lose data (ie your encoding is gone). Therefore, from a CTF standpoint, LSB steganography is only something to look for in PNG photos, not JPEGs. 

# External Resources
Are you so in love with cybersecurity and CTFs that you want to increase your skills outside of class? Here's a list of resources that you can access to learn on your own! If there are others that you're aware of, let us know in the Slack workspace, and we'll add it here! 

* [CTFtime](https://ctftime.org/event/list/upcoming)
    * This resource is first because it's the most important - this webpage has an extensive list of virtual CTFs happening all around the world. This is where we determine which CTF to participate in each month. If you would like to try one on your own or at your own time, you can find one here! Each CTF is different, and some are more difficult than others. 
* [CTF Resources](https://github.com/apsdehal/awesome-ctf)
    * This is a GitHub repo put together by someone else that contains another extensive list of tools that can aid in CTF and cybersecurity challenges - like, extensive...
* [CTF 101](https://ctf101.org/)
    * This provides an overview of a lot of CTF concepts, methods, and challenges that you'll come across or need doing these competitions.
* [RingZer0 CTF](https://ringzer0ctf.com/challenges/)
    * This contains on-demand CTF challenges that you can do, but beware because they're tough!
* [CryptoHack](https://cryptohack.org/)
    * On-demand CTF challenges focusing on cryptography
* [CTFlearn](https://ctflearn.com/)
    * On-demand CTF challenges perfect for beginners. You can choose from a variety of categories and difficulties, and remember, **always look in the comments!**
* [OverTheWire.org Wargames](https://overthewire.org/wargames/)
    * This contains a list of a dozen different cyber wargames you can play to learn skills. Bandit is the first and easiest, and is intended for those who are interested in cybersecurity but haven't used a Linux environment before. Natas is web exploitation-focused. They range in difficulty, and you can only move on to the next level after completing the first one. 
* [TryHackMe](https://tryhackme.com/)
    * Try Hack Me is an online resource where you have access to labs and networks that you can practice your hacking skills on. 
* [HackTheBox](https://www.hackthebox.eu/)
    * Similar to Try Hack Me, Hack the Box has several different boxes where you can challenge yourself and learn new skills.
* [RedTiger](https://redtiger.labs.overthewire.org/)
    * A branch of OverTheWire, RedTiger has 10 levels focused specifically on SQL injection in a PHP environment
* [Hack.me](https://hack.me/s/)
    * This is another resource with on-demand CTF challenges that focus a lot on web exploitation. 
* [INE Pentesting Student Course](https://my.ine.com/path/a223968e-3a74-45ed-884d-2d16760b8bbd)
    * This is one of my favorite online resources. Put on by eLearningSecurity, this is a **completely free** course all about pentesting that covers many of the topics we will be covering, and it prepares you to take the eJPT (eJunior Pentesting) certification afterwards. 
* [Steganography Cheatsheet](https://pequalsnp-team.github.io/cheatsheet/steganography-101)
    * On a steg challenge and you're stuck? This provides a few unique methods to attack steganography problems that may help you. 
* [List of Common Ciphers](http://rumkin.com/tools/cipher/)
    * This is a list of ciphers commonly used in the world, so if you come across a cryptography challenge that you're unfamiliar with, feel free to peruse this list and see if it's one of these!
* [SQL Injection](https://portswigger.net/web-security/sql-injection)
    * This is an amazing resource that PortSwigger (who made Burp Suite) put out about different types of SQL injection and how they work. 
* [Pentest Wiki](https://pentestwiki.org/)
    * Interested in learning some pentesting skills? This wiki has a bunch of great resources to get you started on the Pentesting process. 
* [Password Manager study](https://www.usenix.org/system/files/sec20-oesch_0.pdf)
    * This isn't really CTF-related, but I love it! This is a study done on Password Managers where they compared and contrasted different Password Managers and can help you determine which ones are best.
* [Cybersecurity TEDtalks](https://www.springboard.com/blog/12-must-watch-cybersecurity-ted-talks/)
    * This is a link to 12 cybersecurity-focused TED talks that you can watch whenever you'd like.
* [Cybersecurity Career Descriptions](https://www.learnhowtobecome.org/computer-careers/cyber-security/)
    * Only vaguely related to CTFs, this link is an excellent source for learning about the similarities and differences in cybersecurity careers.
* [SANS CISO Mindmap](https://www.sans.org/security-resources/posters/security-leadership-poster/135/download)
    * This resource, provided by SANS, provides a visual of what a CISO needs to keep in mind, and also the major functions of a Security Operations Center (SOC). 
