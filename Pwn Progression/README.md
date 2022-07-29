# Binary Exploitation (pwn)
What to learn if you are at that level

## Prerequisites (Noob)
* C/C++
    * Functions, conditionals, data types/structures
    * Libraries (externally-linked, ldd, etc.)
    * Compiling and basic binary understanding
        <details>
            <summary><i>Resources</i></summary>

        * [Nightmare/HopperRoppers - Foundational C](https://github.com/hoppersroppers/nightmare/blob/master/modules/00-intro/readme.md)
        </details>
    * Files/file descriptors
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - File Descriptors](https://ir0nstone.gitbook.io/notes/types/stack/exploiting-over-sockets)
        </details>
* Assembly
    * Basic instructions for x86_64
    * Bits, bytes, words, binary, hexadecimal, etc.
    * Registers, stack, heap, memory
        <details>
            <summary><i>Resources</i></summary>

        * [Nightmare/HopperRoppers - Intro to Assembly](https://github.com/hoppersroppers/nightmare/blob/master/modules/01-intro_assembly/readme.md)
        * [Zeyuan Hu - Understanding how function call works](https://zhu45.org/posts/2017/Jul/30/understanding-how-function-call-works/)
        * [YouTube - The Stack](https://www.youtube.com/watch?v=IWQ74f2ot7E&ab_channel=RetroGameMechanicsExplained)
        * [YouTube - The Call Stack](https://www.youtube.com/watch?v=Q2sFmqvpBe0&t=318s&ab_channel=ComputerScience)
        </details>
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
* Basic reverse engineering
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare/HopperRoppers - Intro to Rev](https://github.com/hoppersroppers/nightmare/tree/master/modules/03-beginner_re)
    </details>


## Beginner
### Knowledge
* Can calculate offsets between functions and addresses in executables and the stack
* Understand parts of a dynamically-linked binary
    <details>
        <summary><i>Resources</i></summary>

    * [ir0nstone - PLT and GOT](https://ir0nstone.gitbook.io/notes/types/stack/aslr/plt_and_got)
    </details>
* What an overflow is
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare/HoppersRopper - Overflows](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows#overflows)
    * (Example) [CSAW 2018 Quals - Boi](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/04-bof_variable/csaw18_boi)
    </details>
* Identify vulnerable code
    <details>
        <summary><i>Resources</i></summary>

    * (Example) [HTB Cyber Apocalypse 2022 - Entrypoint problem](https://github.com/evyatar9/Writeups/tree/master/CTFs/2022-HTB_Cyber_Apocalypse/Pwn-Space_Pirate_Entrypoint)
    * (Example) [LITCTF 2022 - save_tyger problem](https://ctftime.org/writeup/34652)
    * (Example) [Tamu '19 - pwn1 problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/04-bof_variable/tamu19_pwn1)
    * (Example) [TokyoWesterns 2017 - Just Do It! problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/04-bof_variable/tw17_justdoit)
    </details>
* Basic shellcode
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare/HoppersRoppers - Shellcode](https://github.com/hoppersroppers/nightmare/blob/master/modules/04-Overflows/unit_03_shell.md)
    * [ir0nstone - Using NOPs in shellcode](https://ir0nstone.gitbook.io/notes/types/stack/nops)
    </details>
* Understand what various security measures can be taken to secure binaries (introduction)
    * ASLR/PIE
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - PIE](https://ir0nstone.gitbook.io/notes/types/stack/pie)
        * [ir0nstone - ASLR](https://ir0nstone.gitbook.io/notes/types/stack/aslr)
        * [Nightmare/HoppersRoppers - ASLR/PIE](https://github.com/hoppersroppers/nightmare/blob/master/modules/04-Overflows/5.1-mitigation_aslr_pie/readme.md)
        </details>
    * NX
        <details>
            <summary><i>Resources</i></summary>

        * [Nightmare/HoppersRoppers - NX/DEP and Why ROP Exists](https://github.com/hoppersroppers/nightmare/blob/master/modules/06-ROP/07_lecture.pdf)
        </details>
    * Stack canaries
    * RELRO
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - RELRO](https://ir0nstone.gitbook.io/notes/types/stack/relro)
        </details>
* How to approach pwn problems
* Understanding gadgets and return-oriented programming (ROP)
    <details>
        <summary><i>Resources</i></summary>

    * [ir0nstone - ROP](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming)
    * [ir0nstone - Gadgets](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/gadgets)
    * [ir0nstone - Calling Conventions](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/calling-conventions)
    * [ExploitDB Paper on ROP](https://www.exploit-db.com/docs/english/28479-return-oriented-programming-(rop-ftw).pdf)
    * [libc database for when not provided](https://libc.blukat.me/)
    * [Python library that implements libc database](https://github.com/guyinatuxedo/The_Night)
    </details>
* Syscalls
    <details>
        <summary><i>Resources</i></summary>
    
    * [ir0nstone - Syscalls](https://ir0nstone.gitbook.io/notes/types/stack/syscalls)
    * [Linux x86_64 Syscall Table](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/)
    </details>

### Tools
* Ghidra
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare/HopperRoppers - Ghidra](https://github.com/hoppersroppers/nightmare/blob/master/modules/02-intro_tooling/ghidra/readme.md)
    </details>
* GDB
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare/HopperRoppers - GDB](https://github.com/hoppersroppers/nightmare/blob/master/modules/02-intro_tooling/gdb-unit_02.md)
    </details>
* Pwntools - basic features
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare - Pwntools intro](https://guyinatuxedo.github.io/02-intro_tooling/pwntools/index.html)
    * [ir0nstone - Processes and communication](https://ir0nstone.gitbook.io/notes/other/pwntools/processes_and_communication)
    * [ir0nstone - Logging and Context](https://ir0nstone.gitbook.io/notes/other/pwntools/logging_and_context)
    * [ir0nstone - Packing](https://ir0nstone.gitbook.io/notes/other/pwntools/packing)
    </details>
* One_gadget
    <details>
        <summary><i>Resources</i></summary>

    * [One_Gadget GitHub Repo](https://github.com/david942j/one_gadget)
    </details>

### Attacks
* Can perform simple, textbook attacks
    * Ret2win/redirection buffer overflow
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - ret2win](https://ir0nstone.gitbook.io/notes/types/stack/ret2win)
        * (Example) [LITCTF 2022 - save_tyger2 problem (ret2win)](https://github.com/CTF-Team-PlusPlusC/LITCTF2022-Writeups/tree/main/save_tyger2)
        * (Example) [HTB Cyber Apocalypse 2022 - Going Deeper problem (flow redirection)](https://heinandre.no/htb-cyber-apocalypse-2022/pwn/space-pirate-going-deeper/)
        * (Example) [CSAW '16 - Warmup problem (ret2win)](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/05-bof_callfunction/csaw16_warmup)
        * (Example) [CSAW '18 - Get It problem (ret2win)](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/05-bof_callfunction/csaw18_getit)
        * (Example) [Tamu '19 - pwn2 problem (partial overwrite, ret2win)](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/15-partial_overwrite/tamu19_pwn2)
        * (Example) [TUCTF '17 - Vulnchat2 problem (partial overwrite, ret2win)](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/15-partial_overwrite/tuctf17_vulnchat2)
        </details>
    * Non-`%n` format string attacks
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - Format string attacks](https://ir0nstone.gitbook.io/notes/types/stack/format-string)
        * (Example) [PicoCTF '18 - Echo](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/10-fmt_strings/pico18_echo)
        * (Example) [TUCTF '17 - Vuln Chat problem (format strings + buffer overflow, ret2win)](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/05-bof_callfunction/tu17_vulnchat)
        </details>
    * Ret2libc/Ret2system buffer overflow
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - ret2libc](https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/ret2libc)
        * [Red Teaming Experiments - ret2libc](https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc)
        * [Nightmare/HoppersRoppers - ret2system and ret2libc](https://github.com/hoppersroppers/nightmare/blob/master/modules/06-ROP/unit_07.md)
        * (Example) [CSAW '19 - Baby Boi](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/08-bof_dynamic/csaw19_babyboi)
        * (Example) [ASIS '17 - Mary Morton problem (canary leak, ret2system)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/14-ret_2_system/asis17_marymorton)
        * (Example) [FacebookCTF '19 - Overfloat (ret2libc, ASLR bypass, double exploit)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/08-bof_dynamic/fb19_overfloat)
        * (Example) [HSCTF '19 - Storytime (ret2libc, ASLR bypass, double exploit, brute force libc)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/08-bof_dynamic/hs19_storytime)
        * (Example) [UTC '19 - Shellme (ret2libc, ASLR bypass, double exploit, brute force libc)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/08-bof_dynamic/utc19_shellme)
        </details>
    * Shell from syscall
        <details>
            <summary><i>Resources</i></summary>

        * (Example) [DEFCON Quals '19 - Speedrun 1 problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/07-bof_static/dcquals19_speedrun1)
        * (Example) [BostonKeyPart2016 - Simple Calc problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/07-bof_static/bkp16_simplecalc)
        </details>
    * Run shellcode on stack
        <details>
            <summary><i>Resources</i></summary>

        * (Example) [CSAW '17 - Pilot problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/06-bof_shellcode/csaw17_pilot)
        * (Example) [Tamu '19 - Pwn3 problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/06-bof_shellcode/tamu19_pwn3)
        * (Example) [TUCTF '18 - Shella Easy problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/06-bof_shellcode/tu18_shellaeasy)
        </details>
    * Basic integer overflow
        <details>
            <summary><i>Resources</i></summary>

        * [HoppersRoppers - Signed/Unsigned Integer Bugs](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/35-integer_exploitation/signed_unsigned)
        * (Example) ['sploitFun Vuln (int overflow, ret2win)](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/35-integer_exploitation/int_overflow_post)
        * (Example) [Integer Overflow Puzle](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/35-integer_exploitation/puzzle)
        </details>
* Use `LD_PRELOAD` (esp. in ret2libc attacks)
* Leverage basic info leaks
    <details>
        <summary><i>Resources</i></summary>

    * [ir0nstone - PIE info leak](https://ir0nstone.gitbook.io/notes/types/stack/pie/pie-exploit)
    * [ir0nstone - ASLR info leak](https://ir0nstone.gitbook.io/notes/types/stack/aslr/aslr-bypass-with-given-leak)
    * (Example) [HTB Cyber Apocalypse 2022 - Retribution problem (bypass PIE + ASLR, ret2libc)](https://matth.dmz42.org/posts/2022/hackthebox-ctf-cyber-apocalypse-2022-intergalactic-chase-pwn/#1-space-pirate-retribution)
    </details>
* GOT overwrite
    <details>
        <summary><i>Resources</i></summary>

    * [ir0nstone - GOT Overwrite](https://ir0nstone.gitbook.io/notes/types/stack/got-overwrite) and [Exploitation](https://ir0nstone.gitbook.io/notes/types/stack/got-overwrite/exploiting-a-got-overwrite)
    </details>
* Bad seed attacks
    <details>
        <summary><i>Resources</i></summary>

    * [Nightmare/HoppersRoppers - Bad Seed](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc#bad-seed)
    * (Example) [H3 Time problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/09-bad_seed/h3_time)
    * (Example) [HSCTF '19 - Tux Talk Show problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/09-bad_seed/hsctf19_tuxtalkshow)
    * (Example) [SunshineCTF '17 - Prepared problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/09-bad_seed/sunshinectf17_prepared)
    </details>


## Intermediate
### Knowledge
* Different architectures (ARM, MIPS, etc.)
* Heap stuff
* Advanced Shellcode
    <details>
        <summary><i>Resources</i></summary>
    
    * [ir0nstone - Reliable shellcode](https://ir0nstone.gitbook.io/notes/types/stack/reliable-shellcode)
    * [Nightmare/HoppersRopper - Shellcode variations](https://github.com/hoppersroppers/nightmare/blob/master/modules/04-Overflows/unit_04.md)
    * (Example) [CSAW '18 - Shellpointcode problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/19-shellcoding_pt1/csaw18_shellpointcode)
    * (Example) [DEFCON Quals '19 - Speedrun 3 problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/19-shellcoding_pt1/defconquals19_s3)
    * (Example) [DEFCON Quals '19 - Speedrun 6 problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/04-Overflows/19-shellcoding_pt1/defconquals19_s6)
    </details>
* Tracing
    <details>
        <summary><i>Resources</i></summary>
    
    * [Nightmare/HopperRoppers - ptrace](https://github.com/hoppersroppers/nightmare/blob/master/modules/02-intro_tooling/ptraceLesson.md)
    </details>


### Tools
* Pwntools - advanced features
    <details>
        <summary><i>Resources</i></summary>

    * [Good guide for understanding more advanced pwntools features (Gallopsled)](https://github.com/Gallopsled/pwntools-tutorial)
    * [ir0nstone - ELFs](https://ir0nstone.gitbook.io/notes/other/pwntools/elf)
    * [ir0nstone - ROP](https://ir0nstone.gitbook.io/notes/other/pwntools/rop)
    * [pwntools docs - ASM](https://docs.pwntools.com/en/stable/asm.html)
    * [pwntools docs - Shellcraft](https://docs.pwntools.com/en/stable/shellcraft.html)
    * [ir0nstone - Shellcode example](https://ir0nstone.gitbook.io/notes/types/stack/shellcode)
    </details>
* GEF
* Ropper
* Qemu

### Attacks
* Heap-based exploits
    * ...
    <details>
        <summary><i>Resources</i></summary>

    * https://ir0nstone.gitbook.io/notes/types/heap
    </details>
* Different architectures (ARM, MIPS, etc.)
    <details>
        <summary><i>Resources</i></summary>

    * (Example) [HXP '18 - Poor Canary problem (ARM arch, canary leak, ret2system)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/14-ret_2_system/hxp18_poorCanary)
    </details>
* Advanced bypasses of defensive techniques (outside of info leak)
    * Bypass canaries
        <details>
            <summary><i>Resources</i></summary>

        * [ir0nstone - Stack canary bypasses](https://ir0nstone.gitbook.io/notes/types/stack/canaries)
        * [Nightmare/HoppersRoppers - Stack smashing and canary bypass](https://github.com/hoppersroppers/nightmare/blob/master/modules/04-Overflows/unit_05.md#stack-smashing-detected)
        * (Example) [DEFCON Quals '16 - Feedme problem (canary brute force, shell from syscall)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/07-bof_static/dcquals16_feedme)
        </details>
    * Bypass ASLR
        <details>
            <summary><i>Resources</i></summary>

        * [Nightmare/HoppersRoppers - Defeating ASLR](https://github.com/hoppersroppers/nightmare/blob/master/modules/04-Overflows/unit_05.md)
        * [Nightmare/HoppersRoppers - Partial Overwrite](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc#partial-overwrite)
        * (Example) [Hacklu '15 - Stack stuff problem (Partial overwrite)](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/15-partial_overwrite/hacklu15_stackstuff)
        </details>
* SROP
    <details>
        <summary><i>Resources</i></summary>

    * [ir0nstone - SROP](https://ir0nstone.gitbook.io/notes/types/stack/syscalls/sigreturn-oriented-programming-srop)
    * [Nightmare/HoppersRoppers - SROP](https://github.com/hoppersroppers/nightmare/blob/master/modules/6.1-MoreROP/readme.md)
    </details>
* Stack pivoting
    <details>
        <summary><i>Resources</i></summary>

    * [ir0nstone - Stack pivoting](https://ir0nstone.gitbook.io/notes/types/stack/stack-pivoting)
    </details>
* Forked binaries
    <details>
        <summary><i>Resources</i></summary>
    
    * [ir0nstone - Forking processes](https://ir0nstone.gitbook.io/notes/types/stack/forking-processes)
    </details>
* Advanced format strings vulnerabilities with `%n`
    <details>
        <summary><i>Resources</i></summary>
    
    * [Nightmare/HoppersRoppers - Format strings](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc#format-strings)
    * (Example) [BackdoorCTF '17 - bbpwn problem](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/10-fmt_strings/backdoor17_bbpwn)
    * (Example) [WatevrCTF '19 - Bet Star problem (format strings + GOT overwrite, ret2system)](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/10-fmt_strings/watevrctf19_betstar)
    * (Example) [TokyoWesterns '16 - Greeting problem (format strings + GOT overwrite, ret2system)](https://github.com/hoppersroppers/nightmare/tree/master/modules/05-CriticalMisc/10-fmt_strings/tw16_greeting)
    </details>
* Perform attacks using multiple exploit techniques, textbook attacks with a twist, or basic attacks with 2 or more defenses to bypass
    <details>
        <summary><i>Resources</i></summary>
    
    * (Example) [CSAW Quals '17 - SVC problem (canary leak, ASLR bypass, ret2libc, double exploit)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/08-bof_dynamic/csawquals17_svc)
    </details>
* Out-of-bounds array index attack
    <details>
        <summary><i>Resources</i></summary>
    
    * (Example) [TUCTF - Guestbook (PIE bypass through index attack, ret2system)](https://github.com/hoppersroppers/nightmare/tree/master/modules/06-ROP/14-ret_2_system/tu_guestbook)
    </details>


## Advanced


## Unknown
* Angr
* Radare2
* Windows (https://github.com/r3p3r/nixawk-awesome-windows-exploitation)
* ret2dlresolve (https://ir0nstone.gitbook.io/notes/types/stack/ret2dlresolve)
* ret2csu (https://ir0nstone.gitbook.io/notes/types/stack/ret2csu)
* ret2plt (https://ir0nstone.gitbook.io/notes/types/stack/aslr/ret2plt-aslr-bypass)