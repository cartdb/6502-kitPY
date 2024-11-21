# The assembler

A bare-bones 6502 assembler. Only supports code and the .byte directive. You can also try to implement illegal opcodes, but some of these have more than one byte for the corresponding instruction, so it does not work.

# The disassembler

A bare-bones 6502 disassembler. If byte does not have matching opcode, it is treated as data, else, it is treated as code. No labels or variables are supported.
