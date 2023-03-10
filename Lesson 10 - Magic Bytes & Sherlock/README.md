# Magic Bytes and Sherlock
## Magic Bytes
All files are really stored as 1s and 0s, but the way that these 1s and 0s should be interpreted can vary. For example, the binary `01000001 01000010 01000011` can be interpreted as `ABC` if it's encoded as ASCII, or it can be interpreted as a dark blue, almost black color `#414243` (see below). To keep track of how files should be interpreted, Windows normally has file extensions after a file name, such as `.txt` or `.png`. What if you are given a file with NO file extension? How can you know what the file extension is?

<img src="414243.png" width="200px">

This is where "magic bytes" come in - you can normally tell what type of file something is based on the first few hexadecimal bytes of it. This is where we introduce a Hex Editor. In Windows, I normally use [HxD Hex Editor](https://mh-nexus.de/en/hxd/) and in Linux I use `xxd`, but there are several options available. In this repository is 8 different file types - open up each one and inspect it in a hex editor. Note the beginning hex bytes. 

To match hex bytes to a file type, you can use a list like [Wikipedia's](https://en.wikipedia.org/wiki/List_of_file_signatures). After a while, you can recognize them no problem. You'll come to recognize JPEGs, PNGs, and ZIP files fairly easily. If you're in Linux, you can use a command called `file` that has a list of recognized file types and can automatically map a file to a type. See below for how the file command can be used on each of the meme files. 

<img src="filetypes.png" width="600px">

Without a file extension, Windows has no idea what to do; Linux normally does, however. That's why you won't see file types like `.txt` as often in Linux systems. This can be helpful in forensics investigations when you are given files, and also in cryptography, reverse engineering, and web exploitation. For example, sometimes you're decrypting something and it just looks like what you have is gibberish. However, if something is compressed using `gzip`, of course it will look like gibberish, but it's real. So never discount random gibberish that you find (**trust me**). 

Another important use of magic bytes is recognizing executables - whenever code like C++ is compiled into machine code (1s and 0s), the resulting file is called an "executable" and typically does not have a file extension. Reverse engineering gives you a random executable and expects you to figure out what it does. While there are many tools that can automatically detect it, doing so with `file` can be very helpful. There are examples in the Executables folder in this lesson folder. Linux executables are known as `ELFs` and `PE32s` are Windows executables. 

### Challenges
I've included a few challenge files in the Challenges folder - can you find the flags??

## Sherlock
[Sherlock](https://github.com/sherlock-project/sherlock) is a fairly simply Python script that you can run with a username to find multiple social media sites for a user. This is used in OSINT - when a username or email is found, you can often pivot to other sites with same or similar usernames by using Sherlock. To install, go ahead and follow the directions listed on the GitHub repo.

To find similar usernames, you can simply list them afterwards, such as `python3 sherlock.py ohcoz ohCoz icook icook10 iansucks iansux`.

### Challenges
My handle is `Legoclones` - where can you find me?