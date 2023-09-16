# Python for CTFs
Learning to use automated scanning, fuzzing, and exploitation tools and scripts is a vital part of CTFs as it can lessen your reconnaissance time and increase your attack surface. However, not ever moving past that area is what we call "script kiddies" - eventually, you need to be able to make your own scripts and tools. This will not only earn you more respect from your hacker community, but it will allow you to progress past the "script kiddie" limit (*don't get me wrong, tools are **good** and **should** be used. Oftentimes, it's necessary to become a script kiddie first. Just don't stay there - get creative :D*).

This lesson will not teach basics of programming or even Python (you can learn about that [here](https://www.w3schools.com/python/default.asp)). We will skip over strings, loops, if statements, functions, lack of variable typing (which is wonderful), spacing instead of code blocks (which is awful, unless you're Micheal), and more. We *will* be covering more in depth parts of Python that allow you unlock the full power and efficiency of this wonderful language. This includes Python modules, functions, and various quirks. Let's get learning!

## Modules
### json
`json` allows you to convert objects to JSON strings and viceversa, mainly used when dealing with JSON files. Let's say you have a 2,000 line log file that you want to sort through and it's in JSON format. This means it's probably all on one line, nested 17 layers deep, and **super** nasty when using `grep`. However, important details can be found in this JSON file. You can easily read it into your Python program as an object and start using built-in filtering options. Here's an example ([json_example.py](json_example.py)):

```python
import json

# read JSON file in
my_array = json.loads(open("example.json", "r").read())

# print basic info about the object
print("There are "+str(len(my_array))+" logs in this JSON file")
print("There are",len(my_array[0].keys()),"keys in each log, and the keys are:")
print(my_array[0].keys())

# print _type of each log
print("\n\nIDs of logs:")
for log in my_array:
    print(log["_id"])
```

This will give you the output:

```
There are 10 logs in this JSON file
There are 3 keys in each log, and the keys are:
dict_keys(['_id', '_type', '_source'])


IDs of logs:
Sample-Dashboard-for-Nginx-(JSON)-Logs
Nginx-Dashboard-json
Traffic-vs.-Location-json
Non-200-Response-Code-vs.-Time-json
Unique-Visits-by-City-json
Unique-Visits-json
Bytes-vs.-Time-json
Total-Requests-json
Total-Requests-by-City-json
Traffic-by-Country-ampersand-OS
```

### sys
I mainly use `sys` when getting command-line arguments for Python scripts I've created. This allows you to create flexible scripts that don't always have hard-coded values, so you can use them with a variety of options. Here's an example ([sys_example.py](sys_example.py)) that prints out your name:

```python
import sys

# get arguments
if len(sys.argv) != 2:
    print("Usage: python3 sys_example.py <NAME>")
    quit()

name = sys.argv[1]

print("Nice to meet you,",name)
```

If you type in the command `python3 sys_example.py`, then it will print out `Usage: python3 sys_example.py <NAME>`. If you instead do `python3 sys_example.py Justin`, it will print out `Nice to meet you, Justin`. You can pass in file names, IP addresses, hostnames, and more!

### base64
Most languages have a built-in function for base64 convertion, but Python does not. In addition, the `base64` module requires that all input be in bytes, not strings, and all output is in bytes. This requires some extra `encode` and `decode` functions to be used, but it's still possible. Here's an example ([b64_example.py](b64_example.py)) of encoding base64, and decoding it is pretty much the inverse:

```python
import base64

my_string = "CTF is life!!"
print(my_string)

byte_encoded_string = my_string.encode("utf-8")
print(byte_encoded_string)

base64_encoded_string_bytes = base64.b64encode(byte_encoded_string)
print(base64_encoded_string_bytes)

base64_encoded_string = base64_encoded_string_bytes.decode("utf-8")
print(base64_encoded_string)


print("\nThis can all be combined into one line:")
print(base64.b64encode(my_string.encode("utf-8")).decode("utf-8"))
```

Output:
```
CTF is life!!
b'CTF is life!!'
b'Q1RGIGlzIGxpZmUhIQ=='
Q1RGIGlzIGxpZmUhIQ==

This can all be combined into one line:
Q1RGIGlzIGxpZmUhIQ==
```

### os and pexpect
`os` is one of my favorite features of Python. Since Python is a server-side language, it can run system commands very easily, all you have to do is import the `os` module and call the `system` function. Here's a simple example:

```python
import os

os.system("whoami")
```

Running this short script will print out your username. Notice how we didn't need to run the print function at all, it automatically printed it out. Very long story short, `os` runs commands as they normally would and doesn't capture the output since it's sent to `stdout`, which appears on your terminal. In fact, if you try to capture the result or print it, you'll only get the exit code (which in this case is `0`). So `os` is *super* nice when you have to run a quick command, but not when you need to capture the output. Enter `pexpect`. 

`pexpect` is my module of choice for capturing command output. It can be kind of tricky to work with sometimes, but when you want to automate complex command running that doesn't allow one-liners, this can come in handy. Here is a CTF problem I debated making, but decided not to and put it here instead ([shells.py](shells.py)):

```python
import pexpect

flag = "ctf{im sure this sucks}"

shell = pexpect.spawn("sh")
shell.setecho(False) # disable printing output of shell commands
shell.sendline("FLAG=\""+flag+"\"") # place flag in shell variable of first shell

TOTAL_SHELLS = 50

for i in range(TOTAL_SHELLS):
    shell.sendline("set -o ignoreeof") # disables CTRL+D
    shell.sendline("sh") # spawn new shell
    shell.sendline("FLAG='you are currently "+str(i+1)+" levels of "+str(TOTAL_SHELLS)+" deep'") # put the level in the FLAG variable of other shells

shell.setecho(True)
shell.interact()
```

This problem has no purpose except to make you type "exit" 50 times in a row until you can issue the command `echo $FLAG` to see the flag. And if you miscount, you gotta start over again! This problem was created in a few lines in Python, and can be solved the same way! Yay for automation!!

Notes:
- `sendline` function sends text plus ENTER, so it's like sending a command
- `send` function sends text without ENTER
- `setecho` function disables or enables output for you
- `interact` function means the script is finished, and the user needs to take care of the rest

A tutorial for pexpect can be found at [pythonforbeginners.com](https://www.pythonforbeginners.com/systems-programming/how-to-use-the-pexpect-module-in-python).

### requests (and BeautifulSoup)
This is the last and one of the **most important modules** that you can learn to use in Python. `requests` allows you to send custom HTTP (web) requests and analyze responses. Tools like the Chromium Debugger Console, Burp Suite, Postman, and more are great, but their automation capabilities are limited. `requests` solves that problem! It can seem somewhat intimidating at first since there are lots of options, but learning it can help you solve some problems that can't be done otherwise. 

The most important function is `request`, which can be called like this:

```python
import requests

# constants
cookies = dict(userid='27')
headers = {
    'Referer': 'https://spoofed.location/haha/getrekt',
    'Content-Type': 'application/x-www-form-urlencoded',
}
URL = "https://example.domain.com/path/to/page.php"
METHOD = "POST"

response = requests.request(METHOD, URL, timeout=4, headers=headers, data=data, cookies=cookies)
#                                        |______________________optional______________________|
```

A script to pull out the "Server" HTTP response header from a list of domain names is included in this repository in [detect_server.py](detect_server.py). Just know that requests can have custom headers, data, timeout, cookies, sessions, and more. It can also pull out response headers, status codes, and more.

Analyzing the output programmatically is a bit more difficult, so we're going to rely on `BeautifulSoup` for that (no idea why it's called that). Tbh I always forget how to use it, so I always rely on [this Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3). I won't go through it because honestly this tutorial kind of goes over it all, but just know that `BeautifulSoup` parses it and allows you to filter by classname, id, element type, extract text and attributes, and more. 

*Quick note - this is how lots of "bots" are made that brute force websites and other criminal things*

## Functions
- exec
- eval
- chr/ord

## Other
### Encodings
Python has ways to encode data like numbers and strings when dealing with non-printable characters or when you want to evade filters. For example, you can encode Unicode characters using `\u0000` or `\U00000000`, ASCII characters with `\x00`, and represent numbers in hexadecimal like `0x00`. Use a reference table like [asciitable.com](asciitable.com) or [unicode-table.com](https://unicode-table.com/en/) to find the corresponding hexadecimal numbers for each character you wish to encode. 

Examples:
```python
>>> '\u0064\u0063'              # unicode to ascii
'dc'
>>> '\x64\x63'                  # hex to ascii
'dc'
>>> '\U00000064\U00000063'      # long unicode to ascii
'dc'
>>> 0x64                        # hex to decimal
100
```

### Local imports
Whenever you see something like `from datetime import datetime`, the "from" refers to the module called datetime and the "import" refers to the function called datetime. Whenever you see `import json`, the "import" refers to the module, and all the functions are imported by default. 

However, that only applies to modules. It's also possible to create local files and import them and functions. If you have two files in the same directory called `library.py` and `main.py`, you could have a line called `from library import function1, function2, function3`. The "from" refers to the name of the file, and the "import" refers to specific functions or variables being imported. This way, you can define functions in another file and use them in your main file, cleaning up your code.

You'll often see `from answer import FLAG` in CTFs specifically, but no file called `answer.py` will be provided. That just means the `FLAG` variable is actually stored in the `answer.py` file and is used in the file provided. This way, you can't see the flag but you can imagine where it would be.

### Importing Modules
Some modules come with a default `python3` install by default, such as `os` and `sys`. However, others are not and need to be imported using `pip3`. `pip3` can be installed on a debian machine by using `sudo apt install python3-pip`. To install a module, simply use the command `sudo pip3 install <MODULE>` like `sudo pip3 install requests`. If you ever see an error like `No module named 'dns'`, just google it and it'll tell you the name of the package to install with `pip3`.

### One-liners
Python's ability to make one-liners is honestly unmatched and can make code so quick to type. One tip for combining multiple lines is by using the semicolon (`;`). While it's not required at the end of lines like most languages, it can be used to combine lines such as `import os; os.system("whoami"); print("Heck yes!!")`.

### More
If you want to get *really* deep into Python, look up `dir()`, builtins, `pyc` files, and the difference between Python2 and Python3.

## Challenges
**Challenge 1** - using the `requests` module, get `byu.edu` and print out how many `<img>` tags are present in it

**Challenge 2** - using `sys` and `base64`, write a script that will take in a string as an argument, then return it as a base64-encoded string

**Challenge 3** - using `sys` and `ord`, write a script that will take in a string as an argument, then return the number equivalent (hex or decimal) of each ASCII character separated by spaces