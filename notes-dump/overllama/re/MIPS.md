To virtualize MIPS, you can use `qemu-mips`, which is installed using the same packages referenced in the [[ARM & Aarch64]] section.

```sh
qemu-mips ./bin-name
```
Or if you need to use files stored in the local directory, you can change root with `-L`
```sh
qemu-mips -L ./ ./bin-name
```

If you want to debug mips, it's a little trickier. First, install `gdb-multiarch`. Then, you can use this script to get qemu-mips to spin up a server:
```python
from pwn import *

# sub either of these files with the associated file path
binary = "./file-to-run"
elf = context.binary = ELF(binary, checksec=False)
qemu = ELF('./qemu-mips',checksec=False)

if args.REMOTE:
    p = remote("localhost", 1337)
else:
    p = qemu.process(['-g','1234','./chall'])
    # you can also add the -L into the process command if necessary
```
Or you can literally just run this command:
```sh
./qemu-mips -g 1234 -L . ./chall
```
Then, in another terminal, run:
`gdb-multiarch -q ./bin-name`
`(gdb) target remote :1234`


[Instruction set cheat sheet](https://www.lri.fr/~de/MIPS.pdf)
- `li R1, const` : `R1` = `const` 32 bit
- `lw R1, const(R2)` : `R1` = `*(R2 + const)` 32 bit
- `addiu R1, R2, const` : `R2` = `R1 + const`
- `move R1 R2` : `R1 = R2`

#### MIPS [[Shell Code]]
You can actually compile and run shellcode for mips in a very similar way to normal, just with qemu
```sh
mips-linux-gnu-gcc -nostdlib -static shellcode.s -o shellcode-mips-elf
qemu-mips-static ./shellcode-mips-elf
```
You can even `strace` with `qemu-mips-static -strace ./shellcode-mips-elf` and gdb with `qemu-mips-static -g 1234 ./shellcode-mips-elf` which will open a port for you to connect to with `gdb-muiltiarch`