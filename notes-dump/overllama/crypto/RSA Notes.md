[Absolute number one RSA paper](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf) - basically I wanna just translate this into layman's terms so I can actually remember it all lol

### The basics
RSA is pretty simple. You have two primes, p and q, of significant length. You public key consists of n, which is p\*q, and e, which is typically 0x10001 or 65537. Encryption is as follows:
	Ciphertext = message<sup>e</sup> mod n
You can decrypt by finding the d value of a number, which is calculated as
	e<sup>-1</sup> mod $\phi$(n)
And decryption is done by:
	message = ciphertext<sup>d</sup> mod n
The difficulty of breaking RSA lies in the fact that it's not easy to factor N, since the private key is just n, d. So if you can find d (typically through finding the factors of n), you can decrypt anything sent with that key
### Coppersmith's Attack
So if you know some "salt" attached to the factors, i.e. rather than being a<sup>e</sup> it's (a+x)<sup>e</sup> where x is known, you can use coppersmith!

Example implementation in sagemath:
```python
p = random_prime(2^512)
q = random_prime(2^512)
n = p*q
a = p - (p % 2^160)

sage: hex(a)
'5d388fc0902ebe38dcd214d13e5be1c89827c5ac8e91c8a97
3320ada8edc33656846143427abe6eb51fb3d6a00000000000
00000000000000000000000000000'

X = 2^160           # matching p % 2^160 above
M = matrix([[X^2, X*a, 0], [0, X, a], [0, 0, n]])
B= M.LLL()

Q = B[0][0]*x^2/X^2+B[0][1]*x/X+B[0][2]

sage: Q.roots(ring=ZZ)
[(281309904423412535115696871561721270073659798137, 1)]
sage: a+Q.roots(ring=ZZ) [0] [0] == p
True
```
We set `X` to the number of unknown bits of A, being the magnitude of our unknown `x`
The associated polynomial, then, is f(x) = (a + x)<sup>3</sup> mod n
### LLL Lattice Reduction
[David Wong](https://www.youtube.com/watch?v=3cicTG3zeVQ&ab_channel=DavidWong)
