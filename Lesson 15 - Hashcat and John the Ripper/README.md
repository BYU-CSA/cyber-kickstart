# Password Cracking
Password cracking is the process of brute forcing passwords that have been stored using a hash function. A hash is a one-way function that takes a password and produces a unique value - this means that you can't reverse the process to recover the password. However, if you know a password and hash it and it matches the hash, then you know the password is correct. For example, if you have a password of `password` and you hash it with a hash function like MD5, you get a hash of `5f4dcc3b5aa765d61d8327deb882cf99`. Only having the hash `5f4dcc3b5aa765d61d8327deb882cf99`, you can't determine the password, but having the hash and the password together, you can.

Some common hashing algorithms are MD5, SHA1, SHA256, SHA512, and bcrypt. In the context of password cracking, the hashing algorithm only matters because some algorithms take longer to compute a hash than others - the longer it takes, the less passwords you can guess per second. As an attacker, it's good to find fast algorithms like MD5, and bad to find hash using slow algorithms like SHA512 or bcrypt.

## Identifying Hashing Algorithms
The easiest way to identify a hashing algorithm used to compute a hash is by the number of characters in the hash. There are some tools that can take in a hash and give you options of possible hashing algorithms. John the Ripper will do this automatically, and there are some online tools ([link 1](https://hashes.com/en/tools/hash_identifier), [link 2](https://www.tunnelsup.com/hash-analyzer/)) and command-line tools that will do this too (see [hash-identifier](https://www.hashidentifier.com/)). This is important because when using password cracking tools, you have to specify which algorithm to use. 

## Choosing a Password Cracking Tool
The two most common password cracking tools are John the Ripper and Hashcat. Both are run through the commandline and are efficient. However, John the Ripper does not support GPU usage and is single-threaded, while Hashcat can be more difficult to use. In addition, John is mainly used in Linux, while Hashcat is mainly used in Windows.

An old version of John the Ripper can be installed from the apt repository by running `sudo apt install john`, while a newer version (called "Jumbo") can be installed through GitHub using the commands below:

```bash
sudo apt-get -y install git build-essential libssl-dev zlib1g-dev yasm pkg-config libgmp-dev libpcap-dev libbz2-dev
cd ~
git clone https://github.com/openwall/john -b bleeding-jumbo john
cd ~/john/src
./configure && make -s clean && make -sj4
```

Hashcat can be installed through the apt repository by running `sudo apt install hashcat`, or online from [hashcat.net](https://hashcat.net/hashcat/).