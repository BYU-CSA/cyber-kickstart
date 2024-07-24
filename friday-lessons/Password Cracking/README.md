# Password Cracking
Password cracking is the process of brute forcing passwords that have been stored using a hash function. A hash is a one-way function that takes a password and produces a unique value - this means that you can't reverse the process to recover the password. However, if you know a password and hash it and it matches the hash, then you know the password is correct. For example, if you have a password of `password` and you hash it with a hash function like MD5, you get a hash of `5f4dcc3b5aa765d61d8327deb882cf99`. Only having the hash `5f4dcc3b5aa765d61d8327deb882cf99`, you can't determine the password, but having the hash and the password together, you can.

Some common hashing algorithms are MD5, SHA1, SHA256, SHA512, and bcrypt. In the context of password cracking, the hashing algorithm only matters because some algorithms take longer to compute a hash than others - the longer it takes, the less passwords you can guess per second. As an attacker, it's good to find fast algorithms like MD5, and bad to find hash using slow algorithms like SHA512 or bcrypt.

So with that context, the art of password cracking is to take a hash and use a tool to compare it to a hashed wordlist of passwords. 

### Identifying Hashing Algorithms
The easiest way to identify a hashing algorithm used to compute a hash is by the number of characters in the hash. There are some tools that can take in a hash and give you options of possible hashing algorithms. John the Ripper will do this automatically, and there are some online tools ([link 1](https://hashes.com/en/tools/hash_identifier), [link 2](https://www.tunnelsup.com/hash-analyzer/)) and command-line tools that will do this too (see [hash-identifier](https://www.hashidentifier.com/)). This is important because when using password cracking tools, you have to specify which algorithm to use. 

### Wordlists
Password cracking only works if the password that you're trying to crack is already on your wordlist. Therefore, as a hacker you've got to have some pretty darn good wordlists if you're going to be effective. The default Kali installation has a bunch of wordlists, but if you're working on a different OS then you can grab some from the internet. The most common is the [rockyou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) list, this is a list of plaintext passwords that was leaked from an old school website called rockyou. If you're really trying to knock your socks off, you can use of the massive [crackstation](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) password lists as well. We'll talk about some tools used to build custom lists down below.

## Common tools
The two most common password cracking tools are John the Ripper and Hashcat. Both are run through the commandline and are efficient. However, John the Ripper does not support GPU usage and is single-threaded, while Hashcat can be more difficult to use. In addition, John is mainly used in Linux, while Hashcat is mainly used in Windows. Most other password cracking tools are used to build custom wordlists for a specific password cracking job. 

* [John the Ripper](https://www.openwall.com/john/)
    * You can find instructions on using John [here](https://www.varonis.com/blog/john-the-ripper). An old version of John the Ripper can be installed from the apt repository by running `sudo apt install john`, while a newer version (called "Jumbo") can be installed through GitHub using the commands below:

    ```bash
    sudo apt-get -y install git build-essential libssl-dev zlib1g-dev yasm pkg-config libgmp-dev libpcap-dev libbz2-dev
    cd ~
    git clone https://github.com/openwall/john -b bleeding-jumbo john
    cd ~/john/src
    ./configure && make -s clean && make -sj4
    ```
* [Hashcat](https://hashcat.net/hashcat/)
    * You can find instructions on using Hashcat [here](https://resources.infosecinstitute.com/topics/hacking/hashcat-tutorial-beginners/). Hashcat can be installed through the apt repository by running `sudo apt install hashcat`, or online from [hashcat.net](https://hashcat.net/hashcat/).
* [CEWL](https://www.geeksforgeeks.org/cewl-tool-creating-custom-wordlists-tool-in-kali-linux/)
    * Cewl is a tool written in Ruby that is designed to scrape the content from a webpage, identify unique words, and build a wordlist from it. You can even configure it to follow links found on the page and go multiple sites deep to develop a robust list on a specific topic. 
* [CUPP](https://github.com/Mebus/cupp)
    * CUPP is tool written in python that will create a custom wordlist based on information that you give about a person. You just input everything that you know about them and CUPP will combine names, dates, and places using common password formats to make a list. 

## Practice Challenges
```md
MD5 (BYU EOS CTF Fall 2021)
--------
We recovered two hashes from a database, and we need you to get the passwords:

`EDBD0EFFAC3FCC98E725920A512881E0`

`67881381DBC68D4761230131AE0008F7`

The flag is in the format `ctf{password1_password2}`

Writeup: https://github.com/BYU-CSA/old-ctf-challenges/tree/master/password-cracking/md5
```

```md
006 III (BYU EOS CTF Winter 2023)
--------
We've finally got a foothold in Janus' network, and we're ready to take them down. This time we've recovered a small batch of passwords that seem to belong to various henchmen in his organisation. We'll need all of them cracked so we can do as much damage as possible this time around. Are you up to the task?

`6328C530F895CA13C75E161DEC260EC2C0BED4FCFF1B34448EA16A7FFFFA5CDC403E5CC83B23321E9AD3280952BE2ADB037DD7AFA3084B7E940C6A655B2F13BA`
`3FAE7E18F9004673D0E68CA10264A1ABAF76FBF42E60D960A1B95289401146E4BF39E599641C730DB8F664F7F1DD02F171BEB4730AC756AAC7CF40C6BC4D623A`
`5C6E3A016FC76F6EC3E062F266977A2C32FD875F0911323256B50A7AA6E24A8C0AD4E6225CA07A73BA1487A83AD7F058CE77345969F1FC04FD6168C15A39EB00`
`A7383D14CF904E91C0F0226CC926CC6CA7CF91F1907025AE961627B444C412247823DA87C3AF69D8A490538554F6E59E972D4EE861726A7B2B3D808CD5096A5B`

Flag format: byuctf{password1_password2_password3_password4}

Writeup: https://github.com/BYU-CSA/old-ctf-challenges/tree/master/password-cracking/006
```

```md
Evolution (BYU EOS CTF Fall 2022)
--------
A password hash to a valuable account was recently discovered in a data leak. It seems this person followed the same pattern for all their passwords, three words. Can you crack this hash?

Note: The flag will be in the form of byuctf{crackedpassword} NO CAPS

`5c558509e482b557e93d169a88f43c4f`

Hint: -o-.jpg
```

## What Next?

* Find some new lists
    * [rockyou2021](https://github.com/ohmybahgosh/RockYou2021.txt) is about the largest I could find, but google away and knock your socks off
* Learn about salts
    * Salting is a process where extra values are added onto each hash to make them harder to crack. You can start learning [here](https://en.wikipedia.org/wiki/Salt_(cryptography)).
* Buy database leaks on the dark web!
    * Just kidding, please don't do that...