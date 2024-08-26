GDB is a [[Linux]] compiled [[C]] debugging tool that is super useful for Rev and PWN challenges in CTFs
microcoruption.com to practice the conceptual stuff

GEF (GDB Enhanced Features) is super useful. Here's how you install it:
```sh
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"
```

Commands that are useful to know
`disass main` will print the assembly for the whole file
`break` or `b` will set a breakpoint at the given location (memory address)
`set $eax = 0xcaf3f00d` will set a register to a value
`set address = value`: sets the value at the address, usually is a dword (4 bytes), but you can modify this by adding `{type}` before address, like `{int}`

You can attach processes to gdb by using the `-p` flag, and using this format will make it really simple to do so: `-p $(pidof ./running_executable)`

crackmes.de is a fun place to practice simple gdb stuff

`info proc mappings` can help you find the heap
`hook-stop` is useful if you want a very specific display whenever you hit a breakpoint (such as the heap or the stack to see it change as you go). This comes in handy when you're working with just normal gdb as well

`ctrl-d` is the way to end a buffer without a `\n` 

You can see environmental variables in gdb using `show env`, and you can unset unwanted ones like `LINES` or `COLUMNS` with `unset env LINES` or set them with `set env LINES value`
The environmental variable `_` stores the last command run. So in a given executable, it should be the absolute path of the executable being run. In gdb, it's gdb, because that is what's being run.

If you want to follow a child rather than the parent, fun `set follow-fork-mode child`

#### GEF
gdb gef has a feature where you can run something like `memory watch 0x7fffffffe500 32 qword` where memory is the name and the `watch` command takes the format `watch <address> [length=0x10] [units=1 byte]`
#### PWNDBG
I've started using pwndbg more than gef because it has a couple things that I really like. First, it automatically will find heap addresses and the location of the main arena rather than making you locate it yourself or add the option of brute forcing it. Second, it will pull glibc and libc source code so you can step through the disas of those functions (like `malloc()` and `free()`) while you have the source code to reference where you are.