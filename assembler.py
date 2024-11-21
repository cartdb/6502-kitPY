import sys
def split_string(string, n):
    return string[:n], string[n:]
if len(sys.argv) == 3:
    if sys.argv[2] == "--illegal":
        instructions = ['BRK impl', 'ORA X,ind', 'JAM', 'SLO X,ind', 'NOP zpg', 'ORA zpg', 'ASL zpg', 'SLO zpg', 'PHP impl', 'ORA #', 'ASL A', 'ANC #', 'NOP abs', 'ORA abs', 'ASL abs', 'SLO abs', 'BPL rel', 'ORA ind,Y', 'JAM', 'SLO ind,Y', 'NOP zpg,X', 'ORA zpg,X', 'ASL zpg,X', 'SLO zpg,X', 'CLC impl', 'ORA abs,Y', 'NOP impl', 'SLO abs,Y', 'NOP abs,X', 'ORA abs,X', 'ASL abs,X', 'SLO abs,X', 'JSR abs', 'AND X,ind', 'JAM', 'RLA X,ind', 'BIT zpg', 'AND zpg', 'ROL zpg', 'RLA zpg', 'PLP impl', 'AND #', 'ROL A', 'ANC #', 'BIT abs', 'AND abs', 'ROL abs', 'RLA abs', 'BMI rel', 'AND ind,Y', 'JAM', 'RLA ind,Y', 'NOP zpg,X', 'AND zpg,X', 'ROL zpg,X', 'RLA zpg,X', 'SEC impl', 'AND abs,Y', 'NOP impl', 'RLA abs,Y', 'NOP abs,X', 'AND abs,X', 'ROL abs,X', 'RLA abs,X', 'RTI impl', 'EOR X,ind', 'JAM', 'SRE X,ind', 'NOP zpg', 'EOR zpg', 'LSR zpg', 'SRE zpg', 'PHA impl', 'EOR #', 'LSR A', 'ALR #', 'JMP abs', 'EOR abs', 'LSR abs', 'SRE abs', 'BVC rel', 'EOR ind,Y', 'JAM', 'SRE ind,Y', 'NOP zpg,X', 'EOR zpg,X', 'LSR zpg,X', 'SRE zpg,X', 'CLI impl', 'EOR abs,Y', 'NOP impl', 'SRE abs,Y', 'NOP abs,X', 'EOR abs,X', 'LSR abs,X', 'SRE abs,X', 'RTS impl', 'ADC X,ind', 'JAM', 'RRA X,ind', 'NOP zpg', 'ADC zpg', 'ROR zpg', 'RRA zpg', 'PLA impl', 'ADC #', 'ROR A', 'ARR #', 'JMP ind', 'ADC abs', 'ROR abs', 'RRA abs', 'BVS rel', 'ADC ind,Y', 'JAM', 'RRA ind,Y', 'NOP zpg,X', 'ADC zpg,X', 'ROR zpg,X', 'RRA zpg,X', 'SEI impl', 'ADC abs,Y', 'NOP impl', 'RRA abs,Y', 'NOP abs,X', 'ADC abs,X', 'ROR abs,X', 'RRA abs,X', 'NOP #', 'STA X,ind', 'NOP #', 'SAX X,ind', 'STY zpg', 'STA zpg', 'STX zpg', 'SAX zpg', 'DEY impl', 'NOP #', 'TXA impl', 'ANE #', 'STY abs', 'STA abs', 'STX abs', 'SAX abs', 'BCC rel', 'STA ind,Y', 'JAM', 'SHA ind,Y', 'STY zpg,X', 'STA zpg,X', 'STX zpg,Y', 'SAX zpg,Y', 'TYA impl', 'STA abs,Y', 'TXS impl', 'TAS abs,Y', 'SHY abs,X', 'STA abs,X', 'SHX abs,Y', 'SHA abs,Y', 'LDY #', 'LDA X,ind', 'LDX #', 'LAX X,ind', 'LDY zpg', 'LDA zpg', 'LDX zpg', 'LAX zpg', 'TAY impl', 'LDA #', 'TAX impl', 'LXA #', 'LDY abs', 'LDA abs', 'LDX abs', 'LAX abs', 'BCS rel', 'LDA ind,Y', 'JAM', 'LAX ind,Y', 'LDY zpg,X', 'LDA zpg,X', 'LDX zpg,Y', 'LAX zpg,Y', 'CLV impl', 'LDA abs,Y', 'TSX impl', 'LAS abs,Y', 'LDY abs,X', 'LDA abs,X', 'LDX abs,Y', 'LAX abs,Y', 'CPY #', 'CMP X,ind', 'NOP #', 'DCP X,ind', 'CPY zpg', 'CMP zpg', 'DEC zpg', 'DCP zpg', 'INY impl', 'CMP #', 'DEX impl', 'SBX #', 'CPY abs', 'CMP abs', 'DEC abs', 'DCP abs', 'BNE rel', 'CMP ind,Y', 'JAM', 'DCP ind,Y', 'NOP zpg,X', 'CMP zpg,X', 'DEC zpg,X', 'DCP zpg,X', 'CLD impl', 'CMP abs,Y', 'NOP impl', 'DCP abs,Y', 'NOP abs,X', 'CMP abs,X', 'DEC abs,X', 'DCP abs,X', 'CPX #', 'SBC X,ind', 'NOP #', 'ISC X,ind', 'CPX zpg', 'SBC zpg', 'INC zpg', 'ISC zpg', 'INX impl', 'SBC #', 'NOP impl', 'USBC #', 'CPX abs', 'SBC abs', 'INC abs', 'ISC abs', 'BEQ rel', 'SBC ind,Y', 'JAM', 'ISC ind,Y', 'NOP zpg,X', 'SBC zpg,X', 'INC zpg,X', 'ISC zpg,X', 'SED impl', 'SBC abs,Y', 'NOP impl', 'ISC abs,Y', 'NOP abs,X', 'SBC abs,X', 'INC abs,X', 'ISC abs,X']
        bytes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
    else:
        instructions = ['BRK impl', 'ORA X,ind', 'ORA zpg', 'ASL zpg', 'PHP impl', 'ORA #', 'ASL A', 'ORA abs', 'ASL abs', 'BPL rel', 'ORA ind,Y', 'ORA zpg,X', 'ASL zpg,X', 'CLC impl', 'ORA abs,Y', 'ORA abs,X', 'ASL abs,X', 'JSR abs', 'AND X,ind', 'BIT zpg', 'AND zpg', 'ROL zpg', 'PLP impl', 'AND #', 'ROL A', 'BIT abs', 'AND abs', 'ROL abs', 'BMI rel', 'AND ind,Y', 'AND zpg,X', 'ROL zpg,X', 'SEC impl', 'AND abs,Y', 'AND abs,X', 'ROL abs,X', 'RTI impl', 'EOR X,ind', 'EOR zpg', 'LSR zpg', 'PHA impl', 'EOR #', 'LSR A', 'JMP abs', 'EOR abs', 'LSR abs', 'BVC rel', 'EOR ind,Y', 'EOR zpg,X', 'LSR zpg,X', 'CLI impl', 'EOR abs,Y', 'EOR abs,X', 'LSR abs,X', 'RTS impl', 'ADC X,ind', 'ADC zpg', 'ROR zpg', 'PLA impl', 'ADC #', 'ROR A', 'JMP ind', 'ADC abs', 'ROR abs', 'BVS rel', 'ADC ind,Y', 'ADC zpg,X', 'ROR zpg,X', 'SEI impl', 'ADC abs,Y', 'ADC abs,X', 'ROR abs,X', 'STA X,ind', 'STY zpg', 'STA zpg', 'STX zpg', 'DEY impl', 'TXA impl', 'STY abs', 'STA abs', 'STX abs', 'BCC rel', 'STA ind,Y', 'STY zpg,X', 'STA zpg,X', 'STX zpg,Y', 'TYA impl', 'STA abs,Y', 'TXS impl', 'STA abs,X', 'LDY #', 'LDA X,ind', 'LDX #', 'LDY zpg', 'LDA zpg', 'LDX zpg', 'TAY impl', 'LDA #', 'TAX impl', 'LDY abs', 'LDA abs', 'LDX abs', 'BCS rel', 'LDA ind,Y', 'LDY zpg,X', 'LDA zpg,X', 'LDX zpg,Y', 'CLV impl', 'LDA abs,Y', 'TSX impl', 'LDY abs,X', 'LDA abs,X', 'LDX abs,Y', 'CPY #', 'CMP X,ind', 'CPY zpg', 'CMP zpg', 'DEC zpg', 'INY impl', 'CMP #', 'DEX impl', 'CPY abs', 'CMP abs', 'DEC abs', 'BNE rel', 'CMP ind,Y', 'CMP zpg,X', 'DEC zpg,X', 'CLD impl', 'CMP abs,Y', 'CMP abs,X', 'DEC abs,X', 'CPX #', 'SBC X,ind', 'CPX zpg', 'SBC zpg', 'INC zpg', 'INX impl', 'SBC #', 'NOP impl', 'CPX abs', 'SBC abs', 'INC abs', 'BEQ rel', 'SBC ind,Y', 'SBC zpg,X', 'INC zpg,X', 'SED impl', 'SBC abs,Y', 'SBC abs,X', 'INC abs,X'] 
        bytes = [0, 1, 5, 6, 8, 9, 10, 13, 14, 16, 17, 21, 22, 24, 25, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 44, 45, 46, 48, 49, 53, 54, 56, 57, 61, 62, 64, 65, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 85, 86, 88, 89, 93, 94, 96, 97, 101, 102, 104, 105, 106, 108, 109, 110, 112, 113, 117, 118, 120, 121, 125, 126, 129, 132, 133, 134, 136, 138, 140, 141, 142, 144, 145, 148, 149, 150, 152, 153, 154, 157, 160, 161, 162, 164, 165, 166, 168, 169, 170, 172, 173, 174, 176, 177, 180, 181, 182, 184, 185, 186, 188, 189, 190, 192, 193, 196, 197, 198, 200, 201, 202, 204, 205, 206, 208, 209, 213, 214, 216, 217, 221, 222, 224, 225, 228, 229, 230, 232, 233, 234, 236, 237, 238, 240, 241, 245, 246, 248, 249, 253, 254]
else:
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
assemble = True
for line in range(len(lines)):
    flag = False
    if len(lines[line]) == 3:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" impl")[0] == lines[line] or instructions[opcode].split(" A")[0] == lines[line]:
                bytesArray.append(bytes[opcode])
                flag = True
            if flag == True:
                break
    elif len(lines[line]) == 9:
        if ".byte $" in lines[line]:
            bytesArray.append(int(lines[line].split(".byte $")[1], 16))
            flag = True
        else:
            for opcode in range(len(instructions)):
                if "USBC #$" in lines[line]:
                    for opc in range(len(instructions)):
                        if instructions[opc] == "USBC #":
                            bytesArray.append(bytes[opc])
                            flag = True
                            break
                    if flag == True:
                        bytesArray.append(int(lines[line].split("USBC #$")[1], 16))
                elif instructions[opcode].split(" abs")[0] in lines[line] and "," not in instructions[opcode] and "," not in lines[line] and len(instructions[opcode].split(" abs")) > 1:
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
                if flag == True:
                    break
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
            if flag == True:
                break  
    elif len(lines[line]) == 8:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" #")[0] in lines[line] and len(instructions[opcode].split(" #")) > 1:
                bytesArray.append(bytes[opcode])
                bytesArray.append(int(lines[line].split("#$")[1], 16))
                flag = True
            if flag == True:
                break
    elif len(lines[line]) == 7:
        for opcode in range(len(instructions)):
            if instructions[opcode].split(" zpg")[0] in lines[line] and "," not in instructions[opcode] and "," not in lines[line] and len(instructions[opcode].split(" zpg")) > 1:
                bytesArray.append(bytes[opcode])
                bytesArray.append(int(lines[line].split("$")[1], 16))
                flag = True
            if flag == True:
                break
    if flag == False:
        print(sys.argv[1] + " (" + str(line + 2) + ") Illegal instruction. - " + lines[line])
        assemble = False
    if len(bytesArray) > 65535:
        print("The file is oversize. Assembling failed.")
        sys.exit()
for byte in range(len(bytesArray)):
    if bytesArray[byte] < 0:
        print(hex(byte))
print(len(bytesArray))
if assemble == True:
    file = open("a.out", "wb")
    file.write(bytearray(bytesArray))
    file.close()
else:
    sys.exit()