Specifically, ARM [[rev fundamentals]] and assembly

### Running the Binary
To run an arm or aarch64 (they're the same thing) on an x86_64 machine, you'll need qemu:
```sh
sudo apt install qemu-user qemu-user-static
```
Once you have this installed, running a binary is as simple as running
```sh
qemu-aarch64 ./bin_name
```
### Compiling for Aarch64
First, you'll need the associated dev tools:
```sh
sudo apt install gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu binutils-aarch64-linux-gnu-dgb
```
Then to compile, you can run:
```sh
aarch64-linux-gnu-gcc -o bin_name bin_name.c
# or
aarch64-linux-gnu-gcc -static -o bin_name bin_name.c
```
### Instructions:
- `stp` : store pair. Format: `stp <sourceReg1>, <sourceReg2>, [destMemAddr]`
- `str` : store. Format: `str <sourceReg>, [destMemAddr]`
- `ldr` : load register. Format:
### Registers:
`x29` : Frame Pointer
`x30` : Link Register