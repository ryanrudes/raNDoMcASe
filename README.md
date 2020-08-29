# raNDoMcASe
An useless, esoteric programming language.

raNDoMcASe is an esoteric, turing-complete programming language based in an equally-ridiculous language, Brain\*\*\*\*.

While it is organized differently, the instructions included in this language serve identical purposes as those in its base-language.

To explain how raNDoMcASe works, it is probably helpful to explain how its base-language works. Brain\*\*\*\* is a minimalist programming language comprised by just 8 instructions. These instructions allow us to make modifications to a stack of memory/data cells, each storing a particular value.
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
 9. `*` (asterisk): Used to both begin and end a loop, which works identically to the `[` and `]` instructions in Brain\*\*\*\*. In raNDoMcASe, you do not need to specify separate instructions for opening and closing the loop; the asterisk serves as both.

Since raNDoMcASe predominantly relies on the *capitalization* of each characterm but not actually on the text itself, one may implant useless messages into there code.

---------

# Hello World! Program
Here is one of many possible "Hello World!" programs in raNDoMcASe, as well as its Brain\*\*\*\* equivalent:

**raNDoMcASe**: `yEeT WHO ARE YOU *oOf CRIES C(oNstANtly) IN yeeTe(d identity)*oOf.Yeet(.com)IS AN EXC(ellent website)*oof VISI(T pls)yEeT a(ll done)*OofW.HE(rE) AM I TO(daY)..(?)HMM(pSt..).YEET Yeet yeet NOW (I'm) BORED*(dead and feeling like) OOf INSI(de...) YEET f(inally, then loop is over. that took a long time to figure out how to write...)* oof.(.. only half-way done) yeet Yeet YEET THESE (yeets) ARE SO(ooo) (rEpEtiTive) *oOf(,) NO PATIENC(e remaining) yeet (almost don)e* oof(... but not that cl)ose.(..) oof (not) Oof (storage) OOF (EFFICIENT!) OOF (ENOUGH!!!).WHY.(?!?)so much.annoying.(..) yeet yeet (we're almost ther)E. Yeet(Again) ANGERERYYY.(ok finally, we're done)` \
**Brain\*\*\*\***: `>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>+.>++++++++++.` \
**Output**: `Hello World!`

How to use:
 1. Place the file *"raNDoMcASe_cOmPiLeR.py"* in the directory: `/usr/local/bin/`
 2. `cd` into the directory with the file, *"raNDoMcASe.sh"*, and execute: `source raNDoMcASe.sh`
 3. Write raNDoMcASe code, and store it in a file with the extension: `.raNDoM`, ie. `MyCode.raNDoM`
 4. Execute the code with: `yeet MyCode.raNDoM`
