
# Lesson 4.5: WeCTF Preparation
--------------------------------------

### Web Only CTF Introduction
  In their words, their vision is to "Help expose some of the latest vulnerabilities in the web technologies, in topics such as side channeling and race condition, SQL injection, and SSRF." It utilizes langauges such as Python, Golang, PHP, C++, Javascript; and services such as Redis, SQLite, Flask, etc.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Review Last Year's Topics
[CTFtime Webpage for 2020 WeCTF](https://ctftime.org/event/1044)
[WeCTF 2020 Source Code](https://github.com/wectf/2020)
You can use the above to breakdown specific challenges and understand what organizers are looking for when they make these problems. 

----------------------------------------------------------------------------------------------------------------------------------------
Here are the challenege writeups by topics, submitted by teams or individuals who competed.

### Race Conditon
[Information on Race Condition](https://www.veracode.com/security/race-condition)
[Faster Shop Writeup by Ekkarin](https://ekkarin-t.medium.com/faster-shop-wectf-2020-write-ups-9f8979cbbe45)

### Prototype Pollution
[Information on Prototype Pollution](https://medium.com/node-modules/what-is-prototype-pollution-and-why-is-it-such-a-big-deal-2dd8d89a93c)
[Light Sequel Writeup by Justins](https://blog.justins.in/wectf-2020/)

### Cross Site Resquest Forgery
[Information on CSRF](https://owasp.org/www-community/attacks/csrf)
[Customer Service by CWGREENE](https://gist.github.com/cwgreene/50d954313e2214c892d4a6d60d882085)

### CRLF Injection
[Information on CRLF Injection](https://www.veracode.com/security/crlf-injection).
[URL Longener By Dshynkev](https://github.com/dshynkev/ctf-writeups/tree/master/2020/wectf/url_longener)

-----------------------------------------------------------------------------------------------------------------------------------------

## General Information on researching Web Vulnerabilities
When it comes to web vulnerabilities, the first resource that comes to mind is the OWASP top 10 Web App vulns. 
This list is updated every year, for 2021 this was the given issues:
  * Injection
  * Broken authentication
  * Sensitive data exposure
  * XML external entities (XXE)
  * Broken access control
  * Security misconfigurations
  * Cross site scripting (XSS)
  * Insecure deserialization
  * Using components with known vulnerabilities
  * Insufficient logging and monitoring

As the years go by, these issues change, although some, such as Security Misconfigurations and Using components with known vulnerabilities are most likely to remain on the list from year to year. It would be well worth your time to familiarize yourself with these topics! 

Other places to learn about web vulnerabilities would include The Sans Institute blog at https://wwww.sans.org/blog. Sans is considered one of the flagship technology institutions and is a phenomenal place to look to for information on Cyber topics and other domains.

Lastly, although they may be more dificult to understand and digest at first, I would definitely recommend scrolling through submitted bug bountry reports and see what professionals are finding on websites and applications today. Hacker101 is the premier site for bugbounty, both for companies to recruit and hackers to work on. Some reports and vulnerabilities are not publically disclosed, however plenty are. There are also good resources in their on site documentation, found here https://www.hacker101.com/resources.

## Conclusion

So in review, WeCTF is a great time to sharpen skills in Web technologies and Exploits. Taking the time to learn about these vulnerabilities helps us to be better cybersecurity 
students and more mindful of the current environment.
