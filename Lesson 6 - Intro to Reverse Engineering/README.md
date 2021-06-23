# Lesson 6 - Intro to Reverse Engineering

## Reverse.cpp
Here is the output for running gdb on the most basic function - just returning 0. 
```
user@computer$ gdb -q ./reverse
Reading symbols from ./reverse...
(gdb) list
1       int main(int argc, char* argv[]) {
2           return 0;
3       }
(gdb) disassemble main
Dump of assembler code for function main(int, char**):
   0x0000000000001125 <+0>:     push   rbp
   0x0000000000001126 <+1>:     mov    rbp,rsp
   0x0000000000001129 <+4>:     mov    DWORD PTR [rbp-0x4],edi
   0x000000000000112c <+7>:     mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001130 <+11>:    mov    eax,0x0
   0x0000000000001135 <+16>:    pop    rbp
   0x0000000000001136 <+17>:    ret    
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x1130: file reverse.cpp, line 2.
```

### Function Prologue
The only line of code in main is `return 0;` , so you would think that would be the first line in assembly. However, you'll notice that lines 0x1125 to 0x1130 have a bunch of random stuff. The compiler adds in a few lines of code to set up the memory for the rest of the functions. These lines are known as the **function prologue**. If you put a breakpoint at the beginning of main, gdb puts it at 0x1130 because it knows that line 2 of code actually starts at memory address 0x1130 (it skips the function prologue). 

#### Function Arguments
At addresses 0x1129 and 0x112c, there are two `mov` commands that involve the edi and rsi registers. In our main function, there are two incoming parameters - an integer (that keeps count of the number of arguments), and a character array (with the arguments). The edi/rdi register is the first parameter passed to a function, and the esi/rsi function has the second parameter. 

Before the main function was called, the argc and argv parameters were put into the edi and rsi registers (respectively). Then, the main function was called. However, since it's possible that the program will need to use the edi and rsi registers later, it needs to store the two arguments locally. 

Addresses 0x1129 and 0x112c store the function arguments locally. This means that if I declare main with **no** arguments, then these two lines wouldn't be here. Address 0x1129 allocates memory for the integer function argument (which we call argc). Where at? Well, the value inside the brackets `[]` indicate where. This integer is stored at `[rbp-0x4]`, or at 4 bytes away from where the rbp register (base pointer) points to. 

So address 0x1129 can be broken up as follows:

```
DWORD PTR [rbp-0x4],edi
    ^         ^      ^ 
I want   | at this | and put 
this much| location| this value
space    |         | in it
```

#### Pushing/Popping the rbp Register
Also note that address 0x1135 pops the rbp register off the stack - this is simply finalizing the function, as it was pushed onto the stack at address 0x1125 in the function prologue.

### Returning Values
Line 2 of code (`return 0;`) correlates with address 0x1130 in the disassemble. The eax/rax register is used to return values from functions. Since we're returning 0, address 0x1130 moves 0 into the eax register, then calls return at address 0x1136. 

Why are we putting 0 into the eax register (32-bit), and not the rax register (64-bit)? We defined the return type for main to be an integer on line 1. Therefore, it doesn't need the rax register, only the shorter eax version. 

## Reverse2.cpp
Here, we've modified our original program a bit. We removed our two main function arguments (argc and argv), but we've initialized a wide variety of variables.

```
$ gdb -q ./reverse2
Reading symbols from ./reverse2...
(gdb) list
1       int main() {
2           // implicit types
3           int a = 0;
4           char b = 'a';
5           bool c = true;
6           float e = 1.2;
7           double f = 4;
8
9           // modified types
10          long int aa = 1;
(gdb) disassemble main
Dump of assembler code for function main():
   0x0000000000001125 <+0>:     push   rbp
   0x0000000000001126 <+1>:     mov    rbp,rsp
   0x0000000000001129 <+4>:     mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000001130 <+11>:    mov    BYTE PTR [rbp-0x5],0x61
   0x0000000000001134 <+15>:    mov    BYTE PTR [rbp-0x6],0x1
   0x0000000000001138 <+19>:    movss  xmm0,DWORD PTR [rip+0xec8]        # 0x2008
   0x0000000000001140 <+27>:    movss  DWORD PTR [rbp-0xc],xmm0
   0x0000000000001145 <+32>:    movsd  xmm0,QWORD PTR [rip+0xec3]        # 0x2010
   0x000000000000114d <+40>:    movsd  QWORD PTR [rbp-0x18],xmm0
   0x0000000000001152 <+45>:    mov    QWORD PTR [rbp-0x20],0x1
   0x000000000000115a <+53>:    mov    WORD PTR [rbp-0x22],0x2
   0x0000000000001160 <+59>:    mov    DWORD PTR [rbp-0x28],0x3
   0x0000000000001167 <+66>:    mov    DWORD PTR [rbp-0x2c],0xffffffff
   0x000000000000116e <+73>:    mov    eax,0x0
   0x0000000000001173 <+78>:    pop    rbp
   0x0000000000001174 <+79>:    ret    
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x1129: file reverse2.cpp, line 3.
```

### Function Prologue and Return
Notice how the function prologue is the same, except that no local space is allocated for function parameters (since there are none). However, rbp is still pushed and popped from the stack, and 0 is still returned through the eax register. 

When we place a breakpoint at main, the program puts it at address 0x1129 because the function prologue ends there, and variables that we specify are being initialized now. 