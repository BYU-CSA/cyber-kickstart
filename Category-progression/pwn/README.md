# Binary Exploitation (pwn)
What to learn if you are at that level

## Prerequisites (Noob)
* C/C++
    * Functions, conditionals, data types/structures
    * Libraries (externally-linked, ldd, etc.)
    * Compiling and basic binary understanding
    * Files/file descriptors
        <details>
            <summary>Resources</summary>

        * [ir0nstone - File Descriptors](https://ir0nstone.gitbook.io/notes/types/stack/exploiting-over-sockets)
        </details>
* Assembly
    * Basic instructions for x86_64
    * Bits, bytes, words, binary, hexadecimal, etc.
    * Registers, stack, heap, memory
    * Objdump
* Basic Python
    * Functions, conditionals
    * Import and use modules
* Basic Operating System knowledge
    * Linux cmds
    * Environmental variables
    * Shells
    * Netcat/ports
* Endianness


## Beginner
### Knowledge
* How to approach pwn problems
* Understand what various security measures can be taken to secure binaries
    * ASLR/PIE
        <details>
            <summary>Resources</summary>

        * [ir0nstone - PIE](https://ir0nstone.gitbook.io/notes/types/stack/pie)
        * [ir0nstone - ASLR](https://ir0nstone.gitbook.io/notes/types/stack/aslr)
        </details>
    * NX
    * Stack canaries
    * RELRO
        <details>
            <summary>Resources</summary>

        * [ir0nstone - RELRO](https://ir0nstone.gitbook.io/notes/types/stack/relro)
        </details>
* Understand parts of a dynamically-linked binary
    <details>
        <summary>Resources</summary>

    * [ir0nstone - PLT and GOT](https://ir0nstone.gitbook.io/notes/types/stack/aslr/plt_and_got)
    </details>
* Understanding gadgets and return-oriented programming (ROP)
    <details>
        <summary>Resources</summary>

    * [ir0nstone - ROP and gadgets](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming)
    </details>
* Can calculate offsets between functions and addresses in executables and the stack
* Identify vulnerable code
    <details>
        <summary>Resources</summary>

    * [HTB Cyber Apocalypse 2022 - Entrypoint problem](https://github.com/evyatar9/Writeups/tree/master/CTFs/2022-HTB_Cyber_Apocalypse/Pwn-Space_Pirate_Entrypoint)
    * [LITCTF 2022 - save_tyger problem](https://ctftime.org/writeup/34652)
    </details>

### Tools
* GDB
* Ghidra
* Pwntools - basic features
    <details>
        <summary>Resources</summary>

    * [Nightmare - Pwntools intro](https://guyinatuxedo.github.io/02-intro_tooling/pwntools/index.html)
    * [ir0nstone - Processes and communication](https://ir0nstone.gitbook.io/notes/other/pwntools/processes_and_communication)
    * [ir0nstone - Logging and Context](https://ir0nstone.gitbook.io/notes/other/pwntools/logging_and_context)
    * [ir0nstone - Packing](https://ir0nstone.gitbook.io/notes/other/pwntools/packing)
    </details>
* One_gadget

### Attacks
* Can perform simple, textbook attacks
    * Ret2win/redirection buffer overflow
        <details>
            <summary>Resources</summary>

        * [ir0nstone - ret2win](https://ir0nstone.gitbook.io/notes/types/stack/ret2win)
        * [LITCTF 2022 - save_tyger2 problem (ret2win)](https://github.com/CTF-Team-PlusPlusC/LITCTF2022-Writeups/tree/main/save_tyger2)
        * [HTB Cyber Apocalypse 2022 - Going Deeper problem (flow redirection)](https://heinandre.no/htb-cyber-apocalypse-2022/pwn/space-pirate-going-deeper/)
        </details>
    * Non-`%n` format string attacks
        <details>
            <summary>Resources</summary>

        * [ir0nstone - Format string attacks](https://ir0nstone.gitbook.io/notes/types/stack/format-string)
        </details>
    * Ret2libc w/ one_gadget
        <details>
            <summary>Resources</summary>

        * 
        </details>
* Use LD_PRELOAD
* Leverage basic info leaks
    <details>
        <summary>Resources</summary>

    * [HTB Cyber Apocalypse 2022 - Retribution problem](https://matth.dmz42.org/posts/2022/hackthebox-ctf-cyber-apocalypse-2022-intergalactic-chase-pwn/#1-space-pirate-retribution)
    </details>
* GOT overwrite
    <details>
        <summary>Resources</summary>

    * [ir0nstone - GOT Overwrite](https://ir0nstone.gitbook.io/notes/types/stack/got-overwrite)
    </details>
* Basic ROP chain


## Intermediate
### Knowledge
* Syscalls
    <details>
        <summary>Resources</summary>
    
    * [ir0nstone - Syscalls](https://ir0nstone.gitbook.io/notes/types/stack/syscalls)
    </details>
* Different architectures (ARM, MIPS, etc.)
* Heap stuff
* Shellcode
    <details>
        <summary>Resources</summary>
    
    * [ir0nstone - Reliable shellcode](https://ir0nstone.gitbook.io/notes/types/stack/relro)
    </details>

### Tools
* Pwntools - advanced features
    <details>
        <summary>Resources</summary>

    * [Good guide for understanding more advanced pwntools features (Gallopsled)](https://github.com/Gallopsled/pwntools-tutorial)
    * [ir0nstone - ELFs](https://ir0nstone.gitbook.io/notes/other/pwntools/elf)
    * [ir0nstone - ROP](https://ir0nstone.gitbook.io/notes/other/pwntools/rop)
    * [pwntools docs - ASM](https://docs.pwntools.com/en/stable/asm.html)
    * [pwntools docs - Shellcraft](https://docs.pwntools.com/en/stable/shellcraft.html)
    * [ir0nstone - Shellcode example](https://ir0nstone.gitbook.io/notes/types/stack/shellcode)
    * [ir0nstone - Using NOPs in shellcode](https://ir0nstone.gitbook.io/notes/types/stack/nops)
    </details>
* GEF
* Ropper
* Qemu

### Attacks
* Heap-based exploits
    * ...
    <details>
        <summary>Resources</summary>

    * https://ir0nstone.gitbook.io/notes/types/heap
    </details>
* Can use gadgets form custom ROP chains
* Different architectures (ARM, MIPS, etc.)
* Bypass canaries
    <details>
        <summary>Resources</summary>

    * [ir0nstone - Stack canary bypasses](https://ir0nstone.gitbook.io/notes/types/stack/canaries)
    </details>
* SROP
    <details>
        <summary>Resources</summary>

    * [ir0nstone - SROP](https://ir0nstone.gitbook.io/notes/types/stack/syscalls/sigreturn-oriented-programming-srop)
    </details>
* Stack pivoting
    <details>
        <summary>Resources</summary>

    * [ir0nstone - Stack pivoting](https://ir0nstone.gitbook.io/notes/types/stack/stack-pivoting)
    </details>
* Forked binaries
    <details>
        <summary>Resources</summary>
    
    * [ir0nstone - Forking processes](https://ir0nstone.gitbook.io/notes/types/stack/forking-processes)
    </details>


## Advanced


## Unknown
* Angr
* Radare2
* Windows
* ret2dlresolve (https://ir0nstone.gitbook.io/notes/types/stack/ret2dlresolve)
* ret2csu (https://ir0nstone.gitbook.io/notes/types/stack/ret2csu)