# Base64
From ImaginaryCTF 2024
We get a simple script that turns the flag into a long data type (which has no upper limit in python) and turns that into a base64 encoded number. This means that the output will be a list of integers that are between 0 and 63, each representing a 6-bit chunk of the plaintext. Because my crypto skills are rusty, it took me a bit to figure that out:
```python
from Crypto.Util.number import bytes_to_long

q = 64                                      

flag = open("flag.txt", "rb").read()
flag_int = bytes_to_long(flag)
secret_key = []

while flag_int:         
	secret_key.append(flag_int % q)
	flag_int //= q                          
print(f"{secret_key = }")
```

With a file called `out.txt`:
```python
secret_key = [10, 52, 23, 14, 52, 16, 3, 14, 37, 37, 3, 25, 50, 32, 19, 14, 48, 32, 35, 13, 54, 12, 35, 12, 31, 29, 7, 29, 38, 61, 37, 27, 47, 5, 51, 28, 50, 13, 35, 29, 46, 1, 51, 24, 31, 21, 54, 28, 52, 8, 54, 30, 38, 17, 55, 24, 41, 1]
```

This is a list of all the 6-bit chunks. We can put them all back together using a simple script:
```python
from Crypto.Util.number import long_to_bytes

secret_key = [10, 52, 23, 14, 52, 16, 3, 14, 37, 37, 3, 25, 50, 32, 19, 14, 48, 32, 35, 13, 54, 12, 35, 12, 31, 29, 7, 29, 38, 61, 37, 27, 47, 5, 51, 28, 50, 13, 35, 29, 46, 1, 51, 24, 31, 21, 54, 28, 52, 8, 54, 30, 38, 17, 55, 24, 41, 1]

plaintext = 0
for val in secret_key[::-1]:
	plaintext *= 64
	plaintext += val

print(long_to_bytes(plaintext))
```

Running this produces:
```shell
jake@atreides (130) > python3 solve.py
b'ictf{b4se_c0nv3rs1on_ftw_236680982d9e8449}\n'
```
