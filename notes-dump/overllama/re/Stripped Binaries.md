If you run info file in gdb, you can get an entry point as well as the markers for all [[ELF]] sections

Usually, the entry point makes a call to `__libc_start_main`, which takes as its first parameter the actual function to be called as main. So whatever gets loaded into `rdi` when `__libc_start_main` is called is your actual main function
You can actually `break _libc_start_main` and it'll break on the start of that function when it is loaded from the shared object. When it breaks, it'll also show you where the main function is located in memory

Statically linked binaries integrate the version of libc they were using into the binary itself so that it can run without libc in path. However, this means that all the libc functions don't have correlated symbols. 
Dealing with a statically linked binary may be best dynamically instead of statically.
Many reverse engineering platforms will have some options to use function signatures to rename existing functions:
- Ghidra: [GitHub - NWMonster/ApplySig: Apply IDA FLIRT signatures for Ghidra](https://github.com/NWMonster/ApplySig)
- Binary Ninja

There's also potential you can let Ghidra start adding symbols for you on analysis (or you can add them yourself) and then you can export that file and have a stripped binary with some custom symbols to help you run it better.