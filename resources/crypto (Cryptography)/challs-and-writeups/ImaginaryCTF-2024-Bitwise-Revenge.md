# Bitwise Revenge
We get a simple python file, pretty similar to Bitwise:
```python
flag='REDACTED'
out = []
for i in flag:
        out.append(str((~ord(i)<<7)^~9))
  
print(out)

# ['13558', '12790', '14966', '13174', '15862', '13302', '15094', '13046', '14838', '14838', '12278', '6390', '12278', '6774', '14070', '12278', '14198', '6262', '14966', '12278', '12534', '12278', '12662', '13558', '14966', '12278', '15350', '13558', '14838', '13046', '16118']
```

This encryption function takes each byte of a flag and:
1. Negate it
2. Left shift by 7
3. XOR by Inverse 9
We can decrypt it by:
1. XOR by inverse 9
2. Right shift by 7
3. Negate it

```python
ciphertext = ['13558', '12790', '14966', '13174', '15862', '13302', '15094', '13046', '14838', '14838', '12278', '6390', '12278', '6774', '14070', '12278', '14198', '6262', '14966', '12278', '12534', '12278', '12662', '13558', '14966', '12278', '15350', '13558', '14838', '13046', '16118']
  
plaintext = []
for byte in ciphertext:
    plaintext.append(chr(~((int(byte) ^ ~9) >> 7)))
  
print("".join(plaintext))
>>> ictf{guess_1_4m_n0t_a_bit_wise}
```
