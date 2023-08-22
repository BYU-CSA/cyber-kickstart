# AES Key Scheduling
Key scheduling is a little complicated when you're first learning about it, but it is designed to be a very simple and very quick calculation. You just have to be able to track all the steps that are occuring. The [Wikipedia article](https://en.wikipedia.org/wiki/AES_key_schedule) for Key Scheduling includes a very useful diagram for understanding this, so we'll use that for our concept map as we explain.

![Key Scheduling Diagram](/mdimg/AES-Key_Schedule_128-bit_key.png)

We start at the top of the diagram with your initial key, split up into a grid four bytes tall and as many across as are necessary for the key length (the example image here shows a key length of 128, but for 192-bit keys it would be 5 across, and 256-bit keys would be 6 across with the same general process).

The permutations between individual round keys is the only part that is particularly complicated, but there are only 3 steps as you can see in the diagram:

### RotWord

For initial context, you are only going to be working with the last column of the last full key (starting out, this is your initial key, but for further rounds, use the last round key)

RotWord is very simple, you take that one by four grid and shift it over one. Example:
```
01    -->  02
02    -->  03
03    -->  04
04    -->  01
```

### SubWord

AES has what is called an S-box. This is a grid that has a substitution value for every possibly combination of 8 bits. Here is is:

![S-Box](/mdimg/s-box.png)

For example, if the value in your vector (post-rotation) is 8d, you would line up the 80 (also represented frequently by '8X') and the 0d ('Xd'). The resulting value that would replace your 8d, then, would be 5d. Do this for each of your four bytes.

### Rcon

Round constants are added to the vector that results from the rotation and subsequent substitution. It gets calculated recursively and will increase with each round of key generation.
 
* rc(1) = 1 (the first round constant is always 1)
* rc(i) = 2 * rc(i-1) if rc(i-1) < 0x80 (156, so if doubling it will make it leave the finite field of 8 bits)
* rc(i) = (2 * rc(i - 1)) xor 0x11b (283) if rc(i-1) >= 0x80 (keep it in the finite field) 

This creates the round constant. So the first round it is 1, then 2, then 4, 8, 10, 20, 40, 80, 1b, 36, etc.

You just add that number to your vector and that sets you up to start the next round key! You will xor that one by four grid you've made with the first vector of your last round key. Then the result of that gets xor'd with the second vector of your last round key. This is visible in the diagram we have of this process, just look at what is being pulled into each of the xor's. (the little plus sign in a circle is an xor).

Let's do an example now to see it in action.

##
Initial key:
```
05 | 67 | 49 | 51
2b | a7 | 32 | 3b
15 | f4 | 82 | 42
94 | 90 | 55 | bc
```
So to get the first vector, we need to rotate, substitute, and add the round constant. 

Rotate:
```
51  --> 3b
3b  --> 42
42  --> bc
bc  --> 51
```
Substitute:         (remember it's just referencing the s-box)
```
3b  --> e2
42  --> 2c
bc  --> 65
51  --> d1
```

Since it's the first round, the round constant is 1, so we just add that to the first value of our vector:
```
e2  --> e3
```

Okay so we have our value to start to xor: e3, 2c, 65, d1. So let's do the xors.
```
e3 ^ 05 --> e6
2c ^ 2b --> 07
65 ^ 15 --> 70
d1 ^ 94 --> 45

# remember that every time you do this, the result is the next addition to the xor

e6 ^ 67 --> 81
07 ^ a7 --> a0
70 ^ f4 --> 84
45 ^ 90 --> d5

81 ^ 49 --> c8
a0 ^ 32 --> 92
84 ^ 82 --> 06 
d5 ^ 55 --> 80

c8 ^ 51 --> 99
92 ^ 3b --> a9
06 ^ 42 --> 44
80 ^ bc --> 3c
```
And that gives us our first round key!
```
e6 | 81 | c8 | 99
07 | a0 | 92 | a9
70 | 84 | 06 | 44
45 | d5 | 80 | 3c
```

This process then will just iterate again with the far right column as our starting point and the round constant increases to 2. Just loop this process until you have all the round keys you need and you have manually completed the Key Scheduling step!

- Further work: how the heck do I implement this in python...