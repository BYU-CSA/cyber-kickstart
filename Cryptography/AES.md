# SYMMETRIC ENCRYPTION
Symmetric encryption is one of the two main types of encryption, the other being asymmetric encryption (for a definition of asymmetric encryption, see [RSA](/RSA.md)). Symmetric encryption only requires one shared key to encrypt and decrypt data, making it faster and more efficient than Asymmetric Encryption. The most commonly used algorithm is the Advanced Encryption Standard (AES).

#
# AES - Advanced Encryption Standard

<details>
    <summary>Various Links and Resources</summary>

* [Computerphile AES Preface](https://youtu.be/VYech-c5Dic?si=9YuixecUyyb7Qvp-)
* [Computerphile AES Overview](https://youtu.be/O4xNJsjtN6E?si=VHQkdWCaTBCUXoGi)
* [Cryptohack](https://cryptohack.org/courses/symmetric/aes0/)
* [cryptopals](https://cryptopals.com/) has some stuff too, start with the Basics
</details>
rijndael algorithm (the algorithm name that won the contest)
AES allows for 128 bit blocks with 128, 192, or 256 bit keys
OpenSSL has a good implementation of AES


Substitution-permutation networks: substitution takes one thing in and puts one thing out (like Ceasar Cipher). Permutation improves that by taking an input and just swapping the bits in a predetermined manner. [Computerphile video](https://youtu.be/DLjzI5dX8jc?si=7YmigjEi77CZKz0i)
Block cipher: takes a block of a certain size and turns it into an output (ciphertext) of the same size


AES functions on the basis of something called a Substitution-Permutation Network ([SP Network](https://youtu.be/DLjzI5dX8jc?si=7YmigjEi77CZKz0i)). 
So each round of AES, there is some kind of substitution (like you would in a ceaser cipher for example) and a permutation (things just get jumbled around). 
AES is a block cipher, meaning it's designed to take a block of a certain bit length at a time, process and encrypt it, and then move on to another block if there was more to the original message. AES has a fixed block size of 128 bits, so it can only encrypt 128 bits at a time before moving on to another block of 128 bits. If the message isn't an exact multiple of 128 bits, padding will be added so it fulfils the block requirement.
Encryption (per block) is performed based on how large your key is. For an 128-bit key, 10 rounds; 192-bit, 12 rounds; 256 bit, 14 rounds. 

To preface any of these rounds, there is a Key Expansion or Key Schedule stage where the key is expanded from the shorter key of 128, 192, or 256 bits into a set of rounds keys. When the process is finished, there will be a key for each round, plus an extra key. So for an 128-bit key, you'll end up with 11 round keys.
You don't neeeeeed to know how to do this but if your curiosity is killing you, you can read a simple explanation [here](/Cryptography/KeySchedule.md).

Once we have our key expanded, we move on to encrypting our actual message with AES. This is the process:

AES typically is implemented as a grid, right so your 128 bit key (split into units of bytes)
```
| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
```
gets turned into a four by four grid like this:
```
| 00 | 04 | 08 | 12 |
| 01 | 05 | 09 | 13 |
| 02 | 06 | 10 | 14 |
| 03 | 07 | 11 | 15 |
```
Knowing that we can understand what AES does to this grid.

Very first thing, the first round key is used in an xor with your plaintext. Then the actual rounds start

1. Substitute bytes

    For each byte, you'll substitute it for another byte. There are no fixed points (no byte gets 'exchanged' with another one, so it's never a one to one conversion. ex: if 62 gets swapped for 45, then 45 cannot be swapped for 62) and every byte switches

1. Shift rows

    The rows of our grid shift. The first row does not rotate, second row from the top moves one left, next row two left, and bottom row moves three left (or one right).

1. Mix columns

    Um the columns get mixed? This gets done with a matrix multiplication. So you multiply each column by a matrix. There is also an 'inverse matrix' that you can use to decrypt it. (This step is skipped in the last round)

    The math is a little complex, but if you'd like to take a look at it you can. The [Wikipedia](https://en.wikipedia.org/wiki/Rijndael_MixColumns) has a pretty in-depth look, and you can find a partial Python implementation as well on [Cryptohack](https://cryptohack.org/courses/symmetric/aes5/)

    One thing you need to remember is that all operations occur in a "finite field" (also known as a Galois field) which is to say that the operands and result must all exist within the field of 2<sup>8</sup> (256, or the maximum integer representation of an 8 bit number). So when you want to 'add' two numbers, you'll actually perform an xor on the numbers. Multiplication is normal just mod a very specific number (this number is 0x11b or 100011011, but there's some pretty neat math behind it if you'd like to take a look this is often represented by x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1 as explained on [Wikipedia](https://en.wikipedia.org/wiki/Finite_field_arithmetic) or briefly on [YouTube](https://youtu.be/9TYfiO__m2A?si=ebY4h4EE1fU4Ytsc))

1. Round key

    The next round key xor'd in.


#
POTENTIAL CHALLENGE: get a key to go through the back half of aes, then decrypt it all the way and they have to push it only through part of aes.

ANOTHER CHALLENGE IDEA: pcap file where a key is sent in plaintext and then aes encrypted text is sent (using the key) in other packets that you have to decrypt