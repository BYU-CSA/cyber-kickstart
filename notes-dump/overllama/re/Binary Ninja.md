I wanna learn how to use this, so here's a note for it:

### Hotkeys
- `[ESC]` : Navigate backward
- `[SPACE]` : Toggle between Linear View and [Graph View](https://docs.binary.ninja/guide/index.html#graph-view)
- `[F5]`, `[TAB]` : Toggle between Pseudo C and Disassembly in the current view
- `g` : Go to an address or symbol
- `n` : Name a symbol
- `;` : Add a comment
- `i` : Cycle between disassembly, LLIL, MLIL and HLIL
- `y` : Change type of the currently selected element
- `a` : Create a C String at the currently selected address
- `1`, `2`, `4`, `8` : Change type of a data variable to the indicated width in bytes (creates a variable if none exists)
- `d` : Switch between data variables of various widths
- `r` : Change the data type to single ASCII character (pressing r in binja will translate hex char to char char)
[Custom hotkeys](https://docs.binary.ninja/guide/index.html#custom-hotkeys)

### Reading IL
Every comparison is either signed (`s<`) or unsigned (`u<`)
Size specifiers:
```
.q -- Qword (8 bytes)
.d -- Dword (4 bytes)
.w -- Word (2 bytes)
.b -- Byte (1 byte)
// floating point has its own, too
.h -- Half (2 bytes)
.s -- Single (4 bytes)
.d -- Double (8 bytes)
.t -- Ten (10 bytes)
.o -- Oword (16 bytes)
```
`sx` is sign extended, `zx` is zero extended. (so signed vs unsigned).

### Plugins

#### Wish list
- [Tanto](https://github.com/Vector35/tanto?tab=readme-ov-file) - lets you do variable slices, so it basically will take a whole function and only show you the lines using a specific variable
- [Snippets](https://github.com/Vector35/snippets) - lets you save and run API python code that isn't big enough to warrant it's own Plugin
- [Sidekick](https://github.com/Vector35/Sidekick-public/tree/main) - AI
- [Opaque Predicate Patcher](https://github.com/Vector35/OpaquePredicatePatcher) - removes conditional branches where the condition is constant
- [Kaitai](https://github.com/Vector35/kaitai) - allows actually good hex analysis
- [6502 Arch Plugin](https://github.com/Vector35/6502) - for NES roms
- [COMpanion](https://github.com/Vector35/COMpanion) - Windows COM objects
- [0CD](https://github.com/0xb0bb/0CD) - make it look actually decent
- [annotate](https://github.com/bkerler/annotate) - auto annotate functions
- [IPython](https://github.com/skr0x1c0/ipybinja) - really nice Binja Python UI
- Okay there are so many community plugins, just scroll through and grab what you want