import sys
def split_string(string, n):
    return string[:n], string[n:]
instructions = ['BRK impl', 'ORA X,ind', 'ORA zpg', 'ASL zpg', 'PHP impl', 'ORA #', 'ASL A', 'ORA abs', 'ASL abs', 'BPL rel', 'ORA ind,Y', 'ORA zpg,X', 'ASL zpg,X', 'CLC impl', 'ORA abs,Y', 'ORA abs,X', 'ASL abs,X', 'JSR abs', 'AND X,ind', 'BIT zpg', 'AND zpg', 'ROL zpg', 'PLP impl', 'AND #', 'ROL A', 'BIT abs', 'AND abs', 'ROL abs', 'BMI rel', 'AND ind,Y', 'AND zpg,X', 'ROL zpg,X', 'SEC impl', 'AND abs,Y', 'AND abs,X', 'ROL abs,X', 'RTI impl', 'EOR X,ind', 'EOR zpg', 'LSR zpg', 'PHA impl', 'EOR #', 'LSR A', 'JMP abs', 'EOR abs', 'LSR abs', 'BVC rel', 'EOR ind,Y', 'EOR zpg,X', 'LSR zpg,X', 'CLI impl', 'EOR abs,Y', 'EOR abs,X', 'LSR abs,X', 'RTS impl', 'ADC X,ind', 'ADC zpg', 'ROR zpg', 'PLA impl', 'ADC #', 'ROR A', 'JMP ind', 'ADC abs', 'ROR abs', 'BVS rel', 'ADC ind,Y', 'ADC zpg,X', 'ROR zpg,X', 'SEI impl', 'ADC abs,Y', 'ADC abs,X', 'ROR abs,X', 'STA X,ind', 'STY zpg', 'STA zpg', 'STX zpg', 'DEY impl', 'TXA impl', 'STY abs', 'STA abs', 'STX abs', 'BCC rel', 'STA ind,Y', 'STY zpg,X', 'STA zpg,X', 'STX zpg,Y', 'TYA impl', 'STA abs,Y', 'TXS impl', 'STA abs,X', 'LDY #', 'LDA X,ind', 'LDX #', 'LDY zpg', 'LDA zpg', 'LDX zpg', 'TAY impl', 'LDA #', 'TAX impl', 'LDY abs', 'LDA abs', 'LDX abs', 'BCS rel', 'LDA ind,Y', 'LDY zpg,X', 'LDA zpg,X', 'LDX zpg,Y', 'CLV impl', 'LDA abs,Y', 'TSX impl', 'LDY abs,X', 'LDA abs,X', 'LDX abs,Y', 'CPY #', 'CMP X,ind', 'CPY zpg', 'CMP zpg', 'DEC zpg', 'INY impl', 'CMP #', 'DEX impl', 'CPY abs', 'CMP abs', 'DEC abs', 'BNE rel', 'CMP ind,Y', 'CMP zpg,X', 'DEC zpg,X', 'CLD impl', 'CMP abs,Y', 'CMP abs,X', 'DEC abs,X', 'CPX #', 'SBC X,ind', 'CPX zpg', 'SBC zpg', 'INC zpg', 'INX impl', 'SBC #', 'NOP impl', 'CPX abs', 'SBC abs', 'INC abs', 'BEQ rel', 'SBC ind,Y', 'SBC zpg,X', 'INC zpg,X', 'SED impl', 'SBC abs,Y', 'SBC abs,X', 'INC abs,X'] 
bytes = [0, 1, 5, 6, 8, 9, 10, 13, 14, 16, 17, 21, 22, 24, 25, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 44, 45, 46, 48, 49, 53, 54, 56, 57, 61, 62, 64, 65, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 85, 86, 88, 89, 93, 94, 96, 97, 101, 102, 104, 105, 106, 108, 109, 110, 112, 113, 117, 118, 120, 121, 125, 126, 129, 132, 133, 134, 136, 138, 140, 141, 142, 144, 145, 148, 149, 150, 152, 153, 154, 157, 160, 161, 162, 164, 165, 166, 168, 169, 170, 172, 173, 174, 176, 177, 180, 181, 182, 184, 185, 186, 188, 189, 190, 192, 193, 196, 197, 198, 200, 201, 202, 204, 205, 206, 208, 209, 213, 214, 216, 217, 221, 222, 224, 225, 228, 229, 230, 232, 233, 234, 236, 237, 238, 240, 241, 245, 246, 248, 249, 253, 254]
file = open(sys.argv[1], "r")
lines = []
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace("\\n", "").replace("\n", "").split(" ;")[0]
    lines.append(line)
bytesArray = []
for line in range(len(lines)):
    flag = False
    if len(lines[line]) == 3:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" impl")[0] == lines[line] or instructions[opcode].split(" A")[0] == lines[line]:
                bytesArray.append(bytes[opcode])
                flag = True
    elif len(lines[line]) == 9:
        if ".byte $" in lines[line]:
            bytesArray.append(int(lines[line].split(".byte $")[1], 16))
            flag = True
        else:
            for opcode in range(len(instructions)):
                if instructions[opcode].split(" abs")[0] in lines[line] and "," not in instructions[opcode] and "," not in lines[line] and len(instructions[opcode].split(" abs")) > 1:
                    bytesArray.append(bytes[opcode])
                    string = lines[line].split("$")[1]
                    high_byte, low_byte = split_string(string, 2)
                    bytesArray.append(int(low_byte, 16))
                    bytesArray.append(int(high_byte, 16))
                    flag = True
                elif instructions[opcode].split(" rel")[0] in lines[line] and len(instructions[opcode].split(" rel")) > 1:
                    bytesArray.append(bytes[opcode])
                    pc = int(hex(len(bytesArray)), 16)
                    branch = int(lines[line].split("$")[1], 16)
                    if pc >= branch:
                        bytesArray.append(int(hex(255 - (pc - branch)), 16))
                    elif pc < branch:
                        bytesArray.append(int(hex((branch - pc) - 1), 16))
                    flag = True
                elif instructions[opcode].split(" zpg,X")[0] in lines[line] and ",X" in lines[line] and len(instructions[opcode].split(" zpg,X")) > 1:
                    bytesArray.append(bytes[opcode])
                    bytesArray.append(int(lines[line].split("$")[1].split(",")[0], 16))
                    flag = True
                elif instructions[opcode].split(" zpg,Y")[0] in lines[line] and ",Y" in lines[line] and len(instructions[opcode].split(" zpg,Y")) > 1:
                    bytesArray.append(bytes[opcode])
                    bytesArray.append(int(lines[line].split("$")[1].split(",")[0], 16))
                    flag = True
    elif len(lines[line]) == 11:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" X,ind")[0] in lines[line] and ",X)" in lines[line] and len(instructions[opcode].split(" X,ind")) > 1:
                bytesArray.append(bytes[opcode])
                bytesArray.append(int(lines[line].split("$")[1].split(",")[0], 16))
                flag = True
            elif instructions[opcode].split(" ind,Y")[0] in lines[line] and "),Y" in lines[line] and len(instructions[opcode].split(" ind,Y")) > 1:
                bytesArray.append(bytes[opcode])
                bytesArray.append(int(lines[line].split("$")[1].split("),")[0], 16))
                flag = True
            elif instructions[opcode].split(" abs,X")[0] in lines[line] and ",X" in lines[line] and "(" not in instructions[opcode] and "(" not in lines[line] and len(instructions[opcode].split(" abs,X")) > 1:
                bytesArray.append(bytes[opcode])
                string = lines[line].split("$")[1].split(",")[0]
                high_byte, low_byte = split_string(string, 2)
                bytesArray.append(int(low_byte, 16))
                bytesArray.append(int(high_byte, 16))
                flag = True
            elif instructions[opcode].split(" abs,Y")[0] in lines[line] and ",Y" in lines[line] and "(" not in instructions[opcode] and "(" not in lines[line] and len(instructions[opcode].split(" abs,Y")) > 1:
                bytesArray.append(bytes[opcode])
                string = lines[line].split("$")[1].split(",")[0]
                high_byte, low_byte = split_string(string, 2)
                bytesArray.append(int(low_byte, 16))
                bytesArray.append(int(high_byte, 16))
                flag = True
            elif instructions[opcode].split(" ind")[0] in lines[line] and "," not in instructions[opcode] and "," not in lines[line] and "(" in lines[line]:
                bytesArray.append(bytes[opcode])
                string = lines[line].split("$")[1].split(")")[0]
                high_byte, low_byte = split_string(string, 2)
                bytesArray.append(int(low_byte, 16))
                bytesArray.append(int(high_byte, 16))
                flag = True     
    elif len(lines[line]) == 8:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" #")[0] in lines[line] and len(instructions[opcode].split(" #")) > 1:
                bytesArray.append(bytes[opcode])
                bytesArray.append(int(lines[line].split("#$")[1], 16))
                flag = True
    elif len(lines[line]) == 7:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" zpg")[0] in lines[line] and "," not in instructions[opcode] and "," not in lines[line] and len(instructions[opcode].split(" zpg")) > 1:
                bytesArray.append(bytes[opcode])
                bytesArray.append(int(lines[line].split("$")[1], 16))
                flag = True
    if flag == False:
        print(sys.argv[1] + " (" + str(line + 2) + ") Illegal instruction. - " + lines[line])
        sys.exit()
    if len(bytesArray) > 65535:
        print("The file is oversize. Assembling failed.")
        sys.exit()
file = open("a.out", "wb")
file.write(bytearray(bytesArray))
file.close()