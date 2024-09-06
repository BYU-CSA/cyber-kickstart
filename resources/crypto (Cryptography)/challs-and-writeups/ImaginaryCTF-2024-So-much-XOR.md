# So much XOR
50pt Crypto challenge [Page 53 of Archived Imaginary CTF Challenges](https://imaginaryctf.org/ArchivedChallenges/53)

We get a simple python script:
```python
from pwn import xor # pwntools xor function
import random
  
flag = open('flag.txt','rb').read()
  
key1 = b'supersecurekey'
key2 = b'verysecretkey'
  
iters1 = random.randint(1,100)
iters2 = random.randint(1,100)
  
enc = flag
for i in range(iters1):
    enc = xor(enc, key1)
    for j in range(iters2):
        enc = xor(enc, key2)
```

As well as some encoded ciphertext: 
```
b'\x1a\x16\x04\x03\t\x00\n<\x18\x07\x06\x03:\x00\x16\x01/\x16\x1d,\t\n\x01\x06\t\x0e\x18'
```

It looks like this script takes a flag from `flag.txt` then chooses 2 random integers between 1 and 100. It then takes two hardcoded keys named `key1` and `key2` and XORs the flag with key2 and key1 a whole bunch of times. The actual behavior doesn't quite matter, as the solve is to take the ciphertext and XOR it with one of the keys to revert it back to it's original state:
```python
from pwn import xor

ciphertext = b'\x1a\x16\x04\x03\t\x00\n<\x18\x07\x06\x03:\x00\x16\x01/\x16\x1d,\t\n\x01\x06\t\x0e\x18'

key1 = b'supersecurekey'
key2 = b'verysecretkey'

xor(key1, ciphertext)
>>> b'ictf{so_much_yet_so_little}'
```

This is possible because for the operation XOR, represented as either $\oplus$  or `^`, and value $a$, both:
$a \oplus a = 0$
$a \oplus 0 = a$
Meaning XORing a value by itself results in 0, and XORing a value by 0 has no effect. This means that this operation can be simplified:
$a \oplus a \oplus a \oplus a$
$(a \oplus a) \oplus (a \oplus a)$
$0 \oplus 0$
$0$

As well as this one:
$a \oplus a \oplus a$
$(a \oplus a) \oplus a$
$0 \oplus a$
$a$

Every pair of xor operations on the same value reduce to 0. it follows that for a chain of XORs on equal values $a$, the result will be zero if the amount of operations is even, and $a$ if the amount of operations is odd.

Notice in step two that XORing two of the same values results in 0, reversing the operation. In this case, the ciphertext is derived in something like this:
$p \oplus flag1 \oplus flag1 \oplus ... \oplus flag2 \oplus flag2 \oplus flag2 = c$

Because each pair of hard coded values effectively cancel each other out, the ciphertext is effectively derived from one of the four possibilities, regardless of how many XOR operations actually exist:
1. $p \oplus flag1 \oplus flag2 = c$
2. $p \oplus flag1 = c$
3. $p \oplus flag2 = c$
4. $p = c$

In this case, it seems that the key was derived from option 2.
