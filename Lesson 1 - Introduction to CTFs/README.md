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

## Challenges
Want to see how well you understand the material? We've provided 3 photos with hidden messages for you to find! See if you can find them all...
