# Lesson 2 - OSINT Fun
OSINT stands for Open Source INTelligence, which is a methodology for collecting, analyzing, and making decisions based on data accessible through publicly available sources. It gives us additional information for [social engineering pretext](https://www.csoonline.com/article/3546299/what-is-pretexting-definition-examples-and-prevention.html), pentesting vectors, and general problem solving. 

## Common Tools
* [OSINT Framework](https://osintframework.com/)
  * A collection of resources used in OSINT, sorted by category (usernames, emails, public records, etc.)
* [DNS Dumpster](https://dnsdumpster.com/)
  * Used to pull information about a website or IP address, such as subdomains, where it's hosted, etc.
* [OSINT Dojo](https://www.osintdojo.com/resources/)
  * A collection of resources to practice OSINT, geared towards CTF participants
* [Sublist3r](https://github.com/aboul3la/Sublist3r)
  * A python script that enumerates subdomains from various sources
* [Namechk](https://namechk.com/)
  * This website is intended to help you find unique usernames, but you can insert a username into it and it will tell you all the websites that the specific username has already been registered in. 
* [Wayback machine](https://archive.org/web/)
  * A website that has been crawling the Internet for decades and holds many old versions of websites in its archives

## Googling
There are many [advanced Googling techniques](https://www.coforge.com/blog/advanced-google-search-tips) that can allow you to be more precise while searching through a website. Google often crawls and indexes entire websites, so if you're doing recon on a website, you can use Google to search through pages already indexed while keeping your IP address out of the site's network logs. 

In addition, it allows you to be more specific when searching for precise information. These include:

* Using an exact phrase
* Excluding a word
* Searching by file type
* Only getting results from a specific website
* And much more!

See the link above for specifics on how to use these skills. 

## Examples
### DNS Dumpster
Searching "justinapplegate.me" on DNS Dumpster gives you the site that he registered his domain with, where his website is hosted, the IP address of the site, and more!

![image](https://user-images.githubusercontent.com/70449145/119071481-210b5580-b9a7-11eb-94ae-9569fb262ffe.png)

### Sublist3r
Running "justinapplegate.me" in sublist3r gives you four subdomains! See how many of them are still there...

![image](https://user-images.githubusercontent.com/70449145/119071701-88290a00-b9a7-11eb-8f70-55cfe13349be.png)

### Advanced Googling
There are 2 results from the site https://justinapplegate.me that are PDFs and **don't** contain the word "america".

![image](https://user-images.githubusercontent.com/70449145/119071813-b9a1d580-b9a7-11eb-8dbe-8b46599f38db.png)

### Internet Archive
This is what BYU's IT&C Department's website looked like in 1999:

![image](https://user-images.githubusercontent.com/70449145/119072018-05ed1580-b9a8-11eb-9aa6-4d68dd85bfad.png)

## Challenges
Want an OSINT challenge to do in your free time? Take a look at [Sourcing Games](https://sourcing.games/) and see how far you can get! 
