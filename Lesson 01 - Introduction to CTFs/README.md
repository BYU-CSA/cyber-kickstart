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


## Challenge types
Some CTFs have unusual categories, but most CTFs have the same types of challenges. [Here](https://ctf101.org/) is a list of the most frequent categories and what types of challenges each category has:

- **Forensics:** The art of recovering the digital trail left on a computer. There are plently of methods to find data which is seemingly deleted, not stored, or covertly recorded.  

- **OSINT:** Open source intelligence, also known as OSINT, refers to the gathering of information from publicly available sources, such as social media, company websites, and news articles. There is a great deal of information that can be gathered about a company or person through open source intelligence.

- **Cryptography:** Breaking widely used encryption schemes which are improperly implemented. The math may seem daunting, but more often than not, a simple understanding of the underlying principles will allow you to find flaws and crack the code.

- **Web Exploitation:** While there are specific vulnerabilities in each programming langage that the developer should be aware of, there are issues fundamental to the internet that can show up regardless of the chosen language or framework. Here you need to exploit a bug to gain some kind of higher level privelege.

- **Reverse Engineering:** Reverse Engineering is typically the process of taking a compiled (machine code, bytecode) program and converting it back into a more human readable format. Very often the goal of a reverse engineering challenge is to understand the functionality of a given program such that you can identify deeper issues.

- **Pwn (Binary Exploitation):** Binaries, or executables, are machine code for a computer to execute. Binary Exploitation is a broad topic within Cyber Security which really comes down to finding a vulnerability in the program and exploiting it to gain control of a shell or modifying the program's functions. For the most part, the binaries that you will face in CTFs are Linux ELF files or the occasional windows executable.


# Resources
There are a few tools and resources that will help you in your journey to become a CTF master.

## Linux
When it comes to cybersecurity and CTF competitions, having access to a Linux environment is at the very least super helpful, if not essential. There are several tools that have not been written for use in a Windows environment. So, what are your options??

* [Installing WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10): WSL stands for "Windows Subsystem for Linux". This tool lets you run linux commands and programs on a Windows desktop. It's pretty awesome and irreplaceable as a CTF tool.

* [Virtual machine](https://itsfoss.com/install-linux-in-virtualbox/): A virtual machine provides a little more power than WSL in running Linux programs. The key difference is that it's completely isolated from your primary operating system. If you want to run a somewhat-sketchy software you found online in order to solve a CTF, definetley do it in a VM, not in WSL!

## Writeups
To really understand how CTF problems are solved and how to approach them, it's best to go over writeups. After many CTFs, participants will make "writeups", where they go through the problem solving process step by step. They'll include screenshots and links to external resources so others who couldn't solve the problem could learn from them. We created a few writeups for challenges that we've solved, and linked them below:

* [baby_python_fixed](https://ctftime.org/writeup/29653) - Jail
* [Tablet 2](https://ctftime.org/writeup/29647) - Web Exploitation
* [Tedious](https://ctftime.org/writeup/29621) - Reverse Engineering
* [Charlie Chaplin 1](https://ctftime.org/writeup/29646) - OSINT

## CTF Time
CTF time is a global scoreboard of all the CTF teams in the world. The BYU team, BYU Cyberia, is usually ranked in the top 30 in the United States and in the top 150 of the world. CTF competitions that other people organize are posted on CTF time so that people worldwide can sign up and compete. Any student at BYU can compete on the BYU Cyberia team-- just create your own CTF time account (using a hacker handle!) and request to join the team.

* [ctftime.org](https://ctftime.org/)

* [View BYU Cyberia team profile](https://ctftime.org/team/155711)

* [View global leaderboard](https://ctftime.org/stats/)

# Practice
Let's jump right in! We will give a walkthrough of some of the following CTF problems. This is on [picoCTF](https://play.picoctf.org/). To follow along, you'll need to make your own picoCTF account. 

- [Crypto - Mod 26](https://play.picoctf.org/practice/challenge/144?category=2&page=1&search=)
- [Web Exploitation - Cookies](https://play.picoctf.org/practice/challenge/173?category=1&page=1&search=)
- [Reverse Engineering - Transformation](https://play.picoctf.org/practice/challenge/104?category=3&page=1&search=)
- [Forensics - Information](https://play.picoctf.org/practice/challenge/186?category=4&page=1&search=)
- [Binary exploitation - Stonks](https://play.picoctf.org/practice/challenge/105?category=6&page=1&search=)
- [Misc - strings](https://play.picoctf.org/practice/challenge/37?category=5&page=1&search=) (Hint: Linux is ___really___ good at this!)