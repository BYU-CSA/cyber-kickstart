Useful pre-dive commands:
```bash
hexdump -C filename
objdump # find man for tags -d -M
strings -n
xxd filename
```
also, `strings -d` will only parse the data section of the ELF
[floss](https://github.com/mandiant/flare-floss/tree/master?tab=readme-ov-file) is a good alternative to strings as well

Before you start analyzing assembly or like function calls or anything like that, get an understanding of what the executable as a whole is doing, and especially where print statements are called and input is passed / checked
`strace <filepath>` will run the file and print out all syscalls made during the execution of the file
`ltrace <filepath>` does the same thing but traces function calls to the standard library

In C, you can make a pointer increment by a value other than its initial data type by re-casting it, then incrementing it. You can even cast it back to the original type to dereference.
```C
ptr = (int *)((char *)ptr + 2 * sizeof(int));
```

`edb` is a graphical debugger in linux
### Resources:
godbolt.org : real-time compiler and assembly analyzer. It can also use whatever compiler and architecture you want