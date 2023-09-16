# OSINT
OSINT stands for **O**pen **S**ource **Int**elligence, which is a methodology for collecting, analyzing, and making decisions based on data accessible through publicly available sources. It gives us additional information for [social engineering pretext](https://www.csoonline.com/article/3546299/what-is-pretexting-definition-examples-and-prevention.html), pentesting vectors, and general problem solving.

The common theory behind OSINT is that everything available online has value and can be combined to create an aggregate sum of information. Learning how to identify what data is available, how it is available and how it can be used are three core tenets to leveraging OSINT. 

Beginners to the CTF world often find OSINT the easiest challenge category to break into, as researching things online is a skill we all use pretty much every day. This lesson is going to introduce you to some techniques and tools you may not know about, and we'll get your hands dirty with a challenge or two, but ultimately getting good at OSINT is all about practice and repetition. 

## Common Tools
* [OSINT Framework](https://osintframework.com/)
  * A collection of resources used in OSINT, sorted by category (usernames, emails, public records, etc.)
* [Google](https://www.google.com/)
  * The most common tool used to find things on the internet, and coincidentally the most powerful. Learning some [advanced Google techniques](https://static.semrush.com/blog/uploads/files/39/12/39121580a18160d3587274faed6323e2.pdf) can bring your searching to the next level
* [Google Maps](https://www.google.com/maps)
  * It's crazy how much you can learn about a physical location just by scoping it out on Maps. You can even look back in time to see what a place used to look like
* [Reverse Image Search (Bing)](https://www4.bing.com/visualsearch)
  * An easy way to search using an image, just upload it and find similar images on the internet. There are many similar search engines, but for whatever reason Bing's is unusually good
* [DNS Dumpster](https://dnsdumpster.com/)
  * Used to pull information about a website or IP address, such as subdomains, where it's hosted, etc.
* [Sublist3r](https://github.com/aboul3la/Sublist3r)
  * A python script that enumerates subdomains from various sources
* [Namechk](https://namechk.com/)
  * This website is intended to help you find unique usernames, but you can insert a username into it, and it will tell you all the websites that the specific username has already been registered in
* [Wayback machine](https://archive.org/web/)
  * A website that has been crawling the Internet for decades and holds many old versions of websites in its archives. This is a super powerful way to see how a website *used* to look

## Practice Challenges

```md
Buckeye Billy Baggage (BYU EOS CTF 2022)
--------
Like a good college student, Buckeye Billy has a great affinity for puzzles, eating right and traveling. In a very college-student-like move, he is often found multitasking. He forgot to tell his roommates where he was off to. Luckily, they found this picture, but it makes no sense. Can you help us find him?
Image: https://github.com/BYU-CSA/old-ctf-challenges/blob/master/OSINT/Buckeye%20Billy%20Baggage/BuckBill2.jpg

flag: byuctf{name_of_landmark}

Writeup: https://github.com/BYU-CSA/old-ctf-challenges/blob/master/OSINT/Buckeye%20Billy%20Baggage/Buckeye%20Billy%20Baggage.md
```

```md
Part of the ship... (SDCTF 2022)
--------
Sometimes I worry about my friend... he's way too into memes, he's always smiling, and he's always spouting nonsense about some "forbidden app." I don't know what he's talking about, but maybe you can help me figure it out! All I know is a username he used way back in the day. Good luck! Flag format is sdctf{flag}  
Username: DanFlashes

Writeup: https://ctftime.org/writeup/33767
```

```md
These People Have No Idea (Unpublished)
--------
These two pictures were taken in Provo UT from the exact same position facing different directions. What is the exact address of the house?

See mountain.png and valley2.0.png in this folder.

Writeup: There isn't one! If you are actually reading this and think you've found it message Dallin Kaufman on Slack.
```

## What Next?

* [OSINT Dojo](https://www.osintdojo.com/resources/)
  * A collection of resources to practice OSINT, geared towards CTF participants. You will *not* be disappointed by looking this thing over, it's got tons of mind maps, resources, ideas to get started, and places to practice
* [Sourcing Games](https://sourcing.games/)
  * Some dude put together a whole bunch of OSINT challenges for people to practice on. It's nice cause you can always check write ups if you get stuck.