# raNDoMcASe
An useless, esoteric programming language.

raNDoMcASe is an esoteric, turing-complete programming language based in Brain****.

While it is organized differently, the instructions included in this language serve identical purposes as those in its base-language.

To explain how raNDoMcASe works, it is probably helpful to explain how its base-language works. Brain**** is a minimalist programming language comprised by just 8 instructions. These instructions allowus to make modifications to a stack of memory/data cells, each storing a particular value.
 1. `>`: Moves the pointer to the right
 2. `<`: Moves the pointer to the left
 3. `+`: Increments the data cell at the pointer
 4. `-`: Decrements the data cell at the pointer
 5. `.` (full stop/period): Outputs the character representation of the cell at the pointer
 6. `,` (comma): Inputs a character and stores it in the cell at the pointer
 7. `[`: If the cell at the pointer is zero, jump to the instruction following the matching `]`. Otherwise, simply continue to the next instruction.
 8. `]`: If the cell at the pointer is nonzero, jump back to the matching `[`. Otherwise, continue to the following instruction.
 
 In raNDoMcASe, the instructions are as follows:

 1. Comments are ignored, and are surrounded by parenthesis: *(I am a comment.)*
 2. Whitespace (spaces, tabs, and new lines) are all ignored, regardless of there placement in the code
 3. `yeet`: Regarding of capitalization (`yeet`, `Yeet`, `yEeT`, etc.), this instruction moves the pointer to the right
 4. `oof`: Regarding of capitalization (`oof`, `Oof`, `OOf`, etc.), this instruction moves the pointer to the left
 5. **Uppercase letters** (`A`, `B`, `C`, ..., `Z`): Increments the data cell at the pointer
 6. **Lowercase Letters** (`a`, `b`, `c`, ..., `z`): Decrements the data cell at the pointer
 7. `.` (full stop/period): Outputs the character representation of the cell at the pointer
 8. `,` (comma): Inputs a character and stores it in the cell at the pointer
 9. `*` (asterisk): Used to both begin and end a loop, which works identically to the `[` and `]` instructions in the Brain****
