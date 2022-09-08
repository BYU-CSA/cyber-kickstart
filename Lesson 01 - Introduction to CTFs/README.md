# Lesson 1 - Introduction to CTFs
Welcome to our GitHub repo where we teach lessons about tools and methods used in Capture the Flag competitions! This is an online resource that you can access whenever you'd like. We plan on including scripts, links, tools, code, examples, and others to help you become more successful in CTFs! Our goal is to have multiple teams progress in our monthly CTF competitions that we participate in, and this is how we plan on doing it!

## Beginners Doc
Not sure what a CTF is or how it works? Don't worry, we've written up [a document](https://github.com/JustinApplegate/ctf-training/blob/main/Beginners.md) that can help answer some of the questions you may have about them. In that beginner document is a list of basic skills that we're assuming (I know, so rude of us!) that you already have. If you aren't comfortable with those skills, we have a list of resources to learn them because they will be essential in using the tools and methods we'll teach. 

## Topics?
What do you want to learn? We've already included a list of [future topics](https://github.com/JustinApplegate/ctf-training/blob/main/Future_Topics.md) that we want to cover, but if there's something in particular you've been *dying* to learn, or something we don't have, let us know in Slack!

# What a CTF looks like
The most common type of CTF, and the type we do here at BYU, is ___Jeapordy-style___ CTFs. In a jeapordy style CTF, you have an online portal with multiple challenges. It looks something like this: 
  
    
![Image of the CTF portal](Portal_View_CTF.jpg)

Each challenge you click on will show both a description of the challenge and a text box for inserting the flag. Follow what the description says, find the flag, and come back and put it in this box. Here is an example of an individual challenge with the submission box:

![Image of an individual challenge on a CTF portal](Individual_Challenge_CTF.jpg)

The screen will tell you if the flag is correct.   
These online CTF portals usually also have a scoreboard so you can see the ranking of your team.

Here are some sites where you can find some on-demand CTF challenges. This is helpful to practice and learn some basic CTF skills. (Notice the challenge portal and what it looks like!)
- [Pico CTF](https://play.picoctf.org/)
- [CTF Learn](https://ctflearn.com/)

## Linux
When it comes to cybersecurity and CTF competitions, having access to a Linux environment is at the very least super helpful, if not essential. There are several tools that have not been written for use in a Windows environment. So, what are your options??

* [Installing WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [Virtual machine](https://itsfoss.com/install-linux-in-virtualbox/)

# Challenge types
Some CTFs have unusual categories, but most CTFs have the same types of challenges. [Here](https://ctf101.org/) is a list of the most frequent categories and what types of challenges each category has:

- **Forensics:** The art of recovering the digital trail left on a computer. There are plently of methods to find data which is seemingly deleted, not stored, or covertly recorded.  

- OSINT
- **Cryptography:** Breaking widely used encryption schemes which are improperly implemented. The math may seem daunting, but more often than not, a simple understanding of the underlying principles will allow you to find flaws and crack the code.

- **Web Exploitation:** While there are specific vulnerabilities in each programming langage that the developer should be aware of, there are issues fundamental to the internet that can show up regardless of the chosen language or framework. Here you need to exploit a bug to gain some kind of higher level privelege.

- Reverse Engineering
- Pwn (Binary Exploitation)


## Writeups
To really understand how CTF problems are solved and how to approach them, it's best to go over writeups. After many CTFs, participants will make "writeups", where they go through the problem solving process step by step. They'll include screenshots and links to external resources so others who couldn't solve the problem could learn from them. We created a few writeups for challenges that we've solved, and linked them below:

* [baby_python_fixed](https://ctftime.org/writeup/29653) - jail
* [Tablet 2](https://ctftime.org/writeup/29647) - web
* [Tedious](https://ctftime.org/writeup/29621) - reverse engineering
* [Charlie Chaplin 1](https://ctftime.org/writeup/29646) - OSINT
