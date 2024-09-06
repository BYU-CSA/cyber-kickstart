# Bitwise
We get a ciphertext in the form of a bunch of negative numbers:
```python
['-111616', '-105472', '-116736', '-102400', '-130048', '-54272', '-93184', '-51200', '-107520', '-93184', '-51200', '-93184', '-106496', '-54272', '-116736', '-93184', '-117760', '-54272', '-121856', '-56320', '-123904']
```

And an encryption function:
```python
out = []
for i in flag:
	out.append(str(~(ord(i) ^ 5) << 10))
print(out)
```

This encryption function takes each byte of the plaintext and:
1. XORs it with 5
2. Negates it
3. Left shifts by 10.

We can use this to decrypt it by taking each byte of the ciphertext and applying the opposite (not necessarily the inverse because the right shift isn't the inverse) operations in revere order:
1. Right shift by 10
2. Negate it
3. XOR with 5
```python
ciphertext = ['-111616', '-105472', '-116736', '-102400', '-130048', '-54272', '-93184', '-51200', '-107520', '-93184', '-51200', '-93184', '-106496', '-54272', '-116736', '-93184', '-117760', '-54272', '-121856', '-56320', '-123904']

plaintext = []                                     

for byte in ciphertext:                            

|   plaintext.append(chr(~(int(byte) >> 10) ^ 5))  

print(''.join(plaintext))
>>> ictf{1_4m_4_b1t_w1s3}
```

