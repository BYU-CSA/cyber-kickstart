# ScisXOR
From ImaginaryCTF archived challenges in round 47:
**Description**: What do you mean the key is too small? 4 characters are enough right?

**Attachments**: 585047514a594644066c544202404068065b00685a004a4a

Our goal will be to figure out which encryption scheme is being used, then use it do decrypt the ciphertext given. We know that the ciphertext is encoded as a hex string. We can turn it back to raw bytes using the `From Hex` operation in Cyberchef. We can guess that the encryption is a simple XOR cipher. XOR (or eXclusive OR), represented by $\oplus$ or `^` is an operation that is reversible. This is an emergent property from the fact that given arbitrary value $a$, both $a \oplus a = 0$ and $a \oplus 0 = a$. 

It's also worth pointing out that XOR is a bit-wise operation. You're probably used to representing numbers in base 10. That means the number 245 is constituted of only 3 parts:
- 2 hundreds - 2 * 100
- 4 tens - 4 * 10
- 5 ones - 5 * 1
You may have heard that computers think in ones and zeros. That means that it represents numbers in base-2 instead of base-10. To a computer, the number 245 is actually made up of 8 parts, based off of the powers of 2 instead of 10:
- 1 128s - 1 * 128
- 1 64s - 1 * 64
- 1 32s - 1 * 32
- 1 16s - 1 * 16
- 0 8s - 0 * 8
- 1 4s - 1 * 4
- 0 2s - 0 * 2
- 1 1s - 1 * 1

We can represent this in binary: 1111 0101. Each one of those ones or zeros is a bit. With a bit wise operation, only a single bit gets affected at a time. This will come up later when we derive a part of the key.

That means that given:
- Plaintext $p$
- Key $k$
- Ciphertext $c$ is $p \oplus k$
$$
p \oplus k = c
$$
If we XOR both sides by the key $k$, it will cancel out:
$$
p \oplus k = c
$$$$
p \oplus k \oplus k = c \oplus k
$$
$$
p \oplus 0 = c \oplus k
$$
$$
p = c \oplus k
$$

This also means we can, only knowing plaintext $p$ and ciphertext $c$, we can derive the key $k$:
$$
p \oplus k = c
$$
$$
p \oplus p \oplus k = c \oplus p
$$
$$
0 \oplus k = c \oplus p
$$
$$
k = c \oplus p
$$

This means that applying the key $k$ to the ciphertext $c$ transforms  it back to the plaintext $p$.

We're going to execute a known plaintext attack. Because we know that the flag probably starts with `ictf{`, we can derive at least part of the key. Let's use cyberchef to easily XOR the ciphertext with `ictf{` encoded as UTF-8 and derive part of the flag.

```
585047514a594644066c544202404068065b00685a004a4a ^ ictf{ = 133710%0`=!v&;e/f3c>,
```

It looks like those first 5 characters that we know are part of the key are `13371`. Lets, try to XOR the ciphertext $c$ with 1337:

```
585047514a594644066c544202404068065b00685a004a4a ^ 1337 = ictf{jus7_gu3ss_7h3_k3y}
```

Success!
