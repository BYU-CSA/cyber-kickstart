# RSA - Rivest Shamir Adleman
Asymmetric Encryption algorithm, uses "commutative" keys to encrypt

Challenge from HSCTF: "What do these numbers mean?"
```python
n = 4155782502547623093831518113976094054382827573251453061239
e = 65537
c = 2669292279100633236493181205299328973407167118230741040683
```

#### Prime Numbers
The most basic RSA Math utilizes prime numbers (having "no" factors) and semi-prime numbers (factors are only prime). As you learn more about advanced cryptography, you'll need to know these terms. Any time you multiply two prime numbers, you get a semi prime number, and those two prime numbers are its only two factors. 'Co-prime' just means that the two numbers in question don't share a common number aside from one. So two prime numbers are co-prime to each other, but 9 and 8 are also co-prime even though they have factors since 9's only factor is 3 and 8's are 4 and 2 (no common factors, or in other terms the gcd is 1).

RSA is an asymmetric encryption algorithm, meaning that it involves two keys, one public and one private. You'll send your public key out to anybody that asks for it, but your private key is yours and yours only. Others will encrypt with your public key to send a message to you, then you will decrypt with your private key.

Here's the mathematical process (simplified):

* Public Key (**p q n t e**)
    Select 2 prime numbers (always **p** and **q**)
    Multiply the two together (becomes a semi-prime number) to get their product, **n**
    To get the totient (**t**) of a semi-prime number, it's just `(p-1)*(q-1)`
        Totient: the number of positive integers <= **n** that are relatively prime to **n**
        This is `phi(n)`, for example, for 7, 6 5 4 3 2 and 1 are relatively prime
        So `phi(7)` is actually 6; `phi(n)` for prime numbers is n-1
        `phi(n)` for semi-prime numbers is `(p-1) * (q-1)` where **p** and **q** are its prime factors
        This means that mathematically, `t = phi(n)`
    The next number, the exponent (**e**), must be prime, less than **t**, and coprime to **t**. The 'standard' **e** is 65537
    This is enough information to create your public key, which is composed of **(n,e)**
    I have done so much reading and it still evades me how this is turned into your base 64 encoded id_rsa.pub file in linux. There are, however, utilities in place for your computer to automatically do the math for you

    You encrypt a message (**m**) by taking the message, converting it to a long int, then you use **n** and **e** to get your cipher text (**c**):
    ```
    m**e % n = c
    ```

    Decryption happens in a very similar way. The idea is \equiv (should make the congruent sign)


* Encrypt
    Message**e % n = cipher text (c)
    Decryption:
        Cipher**d % n = Message


    commutative means it works both ways


Diffie-Hellman
1. Agree on a prime number (p) and a generator of p (g)
2. Randomly generate a private key
3. Public key = g**private % p
4. Exchange public keys
5. Shared_public**private % p == shared secret

Headers are bigger the lower number of # you use
Two asterisks for bold ** or one for italics *
1. Numbers make it a list
* this makes it a bullet points
5. It doesn't matter the numbers it'll organize it anyways lol

[Links are in brackets](followed by a link in parenthesis)
If you want to add code just use `Back ticks`
Add specific code with three back ticks and you can specify the language
```python
x = 10
```
Three or more hyphens, asterisks or underscores will create a division in the page just a big line