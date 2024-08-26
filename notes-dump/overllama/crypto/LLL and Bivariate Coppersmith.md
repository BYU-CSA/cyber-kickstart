So here is the theory for a solve for [[TooManyLeaks - GCC CTF 2024]]:

First, when you remember that exponents are commutative by operation, you can make this set of equations:
    `s == B^a`
    `s2 == (g^a+c)^b == (g^b)^a+c == B^a+c == B^a * B^c == s * B^c`
So we have two equations denoting our knows and unknowns now as well:
    `s = r1 + x1`
    `s2 = r2 + x2`
Where r1 and r2 are known and x1 and x2 are unknown. Since we know B^c because we know B and c, we can rearrange these equations as:
    `r2 + x2 = (r1 + x1) * B^c mod p`
In which we have r1, r2, B^c, and p as known and x1 and x2 as small unknowns
  
The solve relies on something called the LLL algorithm, which is used for lattice-based reduction.
The idea is that if you can get your equation to follow the form k1 + tk2 + u == 0 mod n, you can solve it by creating the matrix:
```
    [n 0 0]
B = [t 1 0]
    [u 0 k]
```
In our case of r2 + x2 = (r1 + x1) * B^c mod p, calling B^c t, we can move the equation round to get:
    `x1 - x2*t^-1 + r1 - r2*t^-1 == 0 mod p`
From that we can get the matrix:
```
    [p 0 0]
B = [t^-1 1 0]
    [r1 - r2*t^-1 0 K]
```
K in this equation is the upper bound for k1 and k2, which in our case is 2^255, since that is the lower limit of our mask
  
SageMath can be used to solve the LLL with their `.LLL()` function on a given matrix. You just need to define the matrix with` SageMath.Matrix()` then run `.LLL()` on it
If you're creating a matrix in the integer space, you just need to run `Matrix(ZZ, matrix)`

Example script:
```python
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
  
#Key in the value of B, c, p, r1, r2, ciphertext, and iv from chall.txt
  
t=pow(B,c,p)
t_inverse = inverse_mod(int(t),int(p))
K=2^255
  
M = Matrix(ZZ, [[p, 0, 0], [t_inverse, 1, 0], [r1-t_inverse*r2, 0, K]])
L = M.LLL()
print(L)
  
#checking which vector has the k1 and k2 value that satisfy the linear equation
for i in range(L.nrows()):
    s2 = r2 + abs(L[i][1])
    s = r1 + abs(L[i][0])
    if(s2%p == s*t%p):
        break
  
sha1 = hashlib.sha1()
sha1.update(str(s).encode('ascii'))
key = sha1.digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(iv))
print(unpad(cipher.decrypt(bytes.fromhex(ciphertext)), 16).decode())
```