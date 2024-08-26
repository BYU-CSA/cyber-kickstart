This note is basically entirely for Cryptanalysis purposes, it'll go very in-depth into the actual process of AES and break it down in such a way that you can break AES yourself when it is sufficiently insecure.
Information pulled from [this site](https://www.davidwong.fr/blockbreakers)

### Key Expansion
For AES-128, it uses an 128 bit key and 11 rounds, so that key must be expanded into a key for 11 rounds of encryption.
There are three functions used for this Key Expansion: `RotWord()`, `SubWord()`, `Rcon()`
#### `RotWord()`
This takes a 4 byte argument and rotates it by 1. So if you have the matrix \[01]\[02]\[03]\[04] it would become \[02]\[03]\[04]\[01], transposed
#### `SubWord()`
This uses an sbox to match the byte inputted by the byte outputted. Essentially, it does a predicted switch of bytes