# AES - Advanced Encryption Standard

### SYMMETRIC ENCRYPTION
Symmetric encryption is one of the two main types of encryption, the other being asymmetric encryption (for a definition of asymmetric encryption, see [RSA](/RSA.md)). Symmetric encryption only requires one shared key to encrypt and decrypt data, making it faster and more efficient than Asymmetric Encryption. The most commonly used algorithm is the Advanced Encryption Standard (AES).

### 
rijndael algorithm (the algorithm name that won the contest)
AES allows for 128 bit blocks with 128, 192, or 256 bit keys
OpenSSL has a good implementation of AES


Substitution-permutation networks: substitution takes one thing in and puts one thing out (like Ceasar Cipher). Permutation improves that by taking an input and just swapping the bits in a predetermined manner. [Computerphile video](https://youtu.be/DLjzI5dX8jc?si=7YmigjEi77CZKz0i)
Block cipher: takes a block of a certain size and turns it into an output (ciphertext) of the same size

[Computerphile AES intro](https://youtu.be/VYech-c5Dic?si=9YuixecUyyb7Qvp-)

AES typically is implemented as a grid, right so your 128 bit key (split into units of bytes)
```
| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
```
gets turned into a four by four grid like this:
| 00 | 04 | 08 | 12 |
|----|----|---|---|
| 01 | 05 | 09 | 13 |
| 02 | 06 | 10 | 14 |
| 03 | 07 | 11 | 15 |

AES functions on the basis of something called a Substitution-Permutation Network (SP Network). So each round of AES, there is some kind of substitution (like you would in a ceaser cipher for example) and a permutation (things just get jumbled around). This is performed in rounds based on how large your key is. For an 128-bit key, 10 rounds; 192-bit, 12 rounds; 256 bit, 14 rounds.

To preface any of these rounds, there is a Key Expansion or Key Schedule stage where the key is expanded from the shorter key of 128, 192, or 256 bits into a set of rounds keys. When the process is finished, there will be a key for each round, plus an extra key. So for an 128-bit key, you'll end up with 11 round keys.
You don't neeeeeed to know how to do this but if your curiosity is killing you, you can read a simple explanation [here](/KeySchedule.md).

1. Substitute bytes
1. Shift rows
1. Mix columns
1. Round key

The initial key gets expanded into a specific key for each round

All operations occur in a "finite field," which is to say that the operands and result must all exist within the field of 2^8 (256, or the maximum integer representation of an 8 bit number)