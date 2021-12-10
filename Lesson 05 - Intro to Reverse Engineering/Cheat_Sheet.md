# Reverse Engineering Cheat Sheet
## Registers
You'll notice how each register has two names - one that starts with an `e`, and one that starts with an `r`. The `e` means it's 32-bit register (ie stores an int), while the `r` means it's a 64-bit register (ie stores a long). This depends on your operating system. Also, in 64-bit systems, you may have r8-15, which aren't named because they came later. 

* `eax/rax` (accumulator) - return values from functions are stored here
* `ecx/rcx` (counter) - multipurpose register
* `edx/rdx` (data) - multipurpose register
* `ebx/rbx` (base) - multipurpose register
* `esp/rsp` (stack pointer) - points to the bottom of the memory segment used by the function. All local variables are stored above this address.
* `ebp/rbp` (base pointer) - points to the base of the memory used by the function. All local variables are stored relative to the address stored here.
* `esi/rsi` (source index) - function argument #2
* `edi/rdi` (destination index) - function argument #1
* `eip/rip` (instruction pointer) - points to the memory address to execute next

## GDB Commands
* `set disassembly-flavor intel` - sets the syntax as Intel instead of AT&T for the current session (recommended)
* `layout asm` - shows you the assembly of the code you're currently running. You can also scroll through the assembly on the screen
* `disassemble main` - prints out the objdump of main
* `layout reg` - shows you the current values of all the registers
* `info registers` -  prints out the values of all the registers (*note - you must run the program first*)
    * `i r` does the same
* `info register xxx` - prints out the value of the specified register (*note - you must run the program first*)
    * `i r xxx` does the same
* `list` - prints out the first 10 lines of text (*note - requires using the `-g` flag when compiling*)
    * `list 5,20` - this prints out lines 5 to 20
    * `show listsize` - shows you how many lines of text are printed out by default with `list`
    * `set listsize 40` - sets the default number of lines printed with `list` to 40
* `break main` - sets a breakpoint at the beginning of main
* `run` - runs the program (until the next breakpoint)
* `ni` - runs the current line of assembly but stops at the next one
* `si` - steps into the current instruction (if a function is called, this allows you to go into the function)
* `call function_name(1234, "string")` - calls a function with your own parameters
* `x 0x01234567` - examines a specific memory address (all options found [here](https://sourceware.org/gdb/current/onlinedocs/gdb/Memory.html))
* `quit` - exits GDB

## Assembly
The overall format is `operation <destination> <source>`. The destination and source are either registers, memory locations, or values. 

## Other
* `echo "set disassembly-flavor intel" > ~/.gdbinit` - sets the syntax as Intel permanently
* Variable names declared while programming do not translate when compiling. In other words, it doesn't matter what you name a variable, the compiler won't record it. This means that when reverse engineering, you won't have variable names, only address locations. 
