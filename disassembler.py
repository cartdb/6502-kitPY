import os 
import sys 
import pathlib 
import zlib
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
file = open(sys.argv[1], "rb")
file = file.read()
file = hex(zlib.crc32(file)).replace("0x", "")
bytesArr = [] 
for byte in pathlib.Path(sys.argv[1]).read_bytes(): 
    bytesArr.append(byte) 
fileBytes = 0 
fileoutput = open(sys.argv[1].replace(os.path.splitext(sys.argv[1])[1], ".asm"), "w")
linesWritten = False
if os.path.getsize(sys.argv[1]) > 65535:
    print("File is too large. It should be chunked up.")
    sys.exit()
while fileBytes < len(bytesArr):
    if fileBytes < 16:
        counter = "000" + hex(fileBytes).replace("0x", "") + " "
    elif fileBytes < 256:
        counter = "00" + hex(fileBytes).replace("0x", "") + " "
    elif fileBytes < 4096:
        counter = "0" + hex(fileBytes).replace("0x", "") + " "
    else:
        counter = hex(fileBytes).replace("0x", "") + " "
    if bytesArr[fileBytes] < 16: 
        instruction = ".byte $0" + hex(bytesArr[fileBytes]).replace("0x", "") 
    else: 
        instruction = ".byte $" + hex(bytesArr[fileBytes]).replace("0x", "") 
    highByte = ""
    lowByte = ""
    try:
        for byte in range(len(bytes)): 
            if bytes[byte] == bytesArr[fileBytes]: 
                if " A" in instructions[byte]: 
                    instruction = instructions[byte].split(" A")[0] 
                elif " abs" in instructions[byte] and "," not in instructions[byte]: 
                    instruction = instructions[byte].split(" abs")[0] 
                    highByte = bytesArr[fileBytes + 2] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    lowByte = bytesArr[fileBytes + 1]
                    if lowByte < 16: 
                        lowByte = "0" + hex(lowByte).replace("0x", "") 
                    else: 
                        lowByte = hex(lowByte).replace("0x", "") 
                    instruction = instruction + " $" + highByte + lowByte 
                    fileBytes += 2
                elif " abs,X" in instructions[byte]: 
                    instruction = instructions[byte].split(" abs,X")[0] 
                    highByte = bytesArr[fileBytes + 2] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    lowByte = bytesArr[fileBytes + 1]
                    if lowByte < 16: 
                        lowByte = "0" + hex(lowByte).replace("0x", "") 
                    else: 
                        lowByte = hex(lowByte).replace("0x", "") 
                    instruction = instruction + " $" + highByte + lowByte + ",X" 
                    fileBytes += 2
                elif " abs,Y" in instructions[byte]: 
                    instruction = instructions[byte].split(" abs,Y")[0] 
                    highByte = bytesArr[fileBytes + 2] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    lowByte = bytesArr[fileBytes + 1]
                    if lowByte < 16: 
                        lowByte = "0" + hex(lowByte).replace("0x", "") 
                    else: 
                        lowByte = hex(lowByte).replace("0x", "") 
                    instruction = instruction + " $" + highByte + lowByte + ",Y"
                    fileBytes += 2 
                elif " #" in instructions[byte]: 
                    instruction = instructions[byte].split(" #")[0] 
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    instruction = instruction + " #$" + highByte 
                    fileBytes += 1 
                elif " impl" in instructions[byte]: 
                    instruction = instructions[byte].split(" impl")[0] 
                elif " ind" in instructions[byte] and "," not in instructions[byte]: 
                    instruction = instructions[byte].split(" ind")[0] 
                    highByte = bytesArr[fileBytes + 2] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    lowByte = bytesArr[fileBytes + 1]
                    if lowByte < 16: 
                        lowByte = "0" + hex(lowByte).replace("0x", "") 
                    else: 
                        lowByte = hex(lowByte).replace("0x", "") 
                    instruction = instruction + " ($" + highByte + lowByte + ")"
                    fileBytes += 2 
                elif " X,ind" in instructions[byte]: 
                    instruction = instructions[byte].split(" X,ind")[0] 
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    instruction = instruction + " ($" + highByte + ",X)" 
                    fileBytes += 1 
                elif " ind,Y" in instructions[byte]: 
                    instruction = instructions[byte].split(" ind,Y")[0] 
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    instruction = instruction + " ($" + highByte + "),Y" 
                    fileBytes += 1 
                elif " rel" in instructions[byte]: 
                    instruction = instructions[byte].split(" rel")[0]  
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte > 127:
                        highByte = hex(fileBytes + 1 - (255 - highByte)).replace("0x", "") 
                    else: 
                        highByte = hex(fileBytes + highByte + 2).replace("0x", "") 
                    if int(highByte, 16) < 16:
                        highByte = "000" + highByte
                    elif int(highByte, 16) < 256:
                        highByte = "00" + highByte
                    elif int(highByte, 16) < 4096:
                        highByte = "0" + highByte
                    instruction = instruction + " $" + highByte 
                    highByte = hex(bytesArr[fileBytes + 1]).replace("0x", "")
                    fileBytes += 1
                elif " zpg" in instructions[byte] and "," not in instructions[byte]: 
                    instruction = instructions[byte].split(" zpg")[0] 
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    instruction = instruction + " $" + highByte 
                    fileBytes += 1 
                elif " zpg,X" in instructions[byte]: 
                    instruction = instructions[byte].split(" zpg,X")[0] 
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    instruction = instruction + " $" + highByte + ",X" 
                    fileBytes += 1 
                elif " zpg,Y" in instructions[byte]: 
                    instruction = instructions[byte].split(" zpg,Y")[0] 
                    highByte = bytesArr[fileBytes + 1] 
                    if highByte < 16: 
                        highByte = "0" + hex(highByte).replace("0x", "") 
                    else: 
                        highByte = hex(highByte).replace("0x", "") 
                    instruction = instruction + " $" + highByte + ",Y" 
                    fileBytes += 1 
                break
    except:
        if bytesArr[fileBytes] < 16: 
            instruction = ".byte $0" + hex(bytesArr[fileBytes]).replace("0x", "") 
        else: 
            instruction = ".byte $" + hex(bytesArr[fileBytes]).replace("0x", "") 
    if highByte != "" and lowByte == "":
        main = hex(bytesArr[fileBytes - 1]).replace("0x", "")
        high = hex(int(highByte, 16)).replace("0x", "")
        if int(main, 16) < 16:
            main = "0" + main
        if int(high, 16) < 16:
            high = "0" + high
        counter = counter + main + " " + high
    elif highByte != "" and lowByte != "":
        main = hex(bytesArr[fileBytes - 2]).replace("0x", "")
        low = hex(int(lowByte, 16)).replace("0x", "")
        high = hex(int(highByte, 16)).replace("0x", "")
        if int(main, 16) < 16:
            main = "0" + main
        if int(low, 16) < 16:
            low = "0" + low
        if int(high, 16) < 16:
            high = "0" + high
        counter = counter + main + " " + low + " " + high
    elif highByte == "" and lowByte == "":
        main = hex(bytesArr[fileBytes]).replace("0x", "")
        if int(main, 16) < 16:
            main = "0" + main
        counter = counter + main
    if linesWritten == False:
        fileoutput.write(instruction + " ; $" + counter) 
        linesWritten = True
    else:
        fileoutput.write("\n" + instruction + " ; $" + counter) 
    fileBytes += 1 
fileoutput.close() 
os.system('python assembler.py "' + sys.argv[1].replace(os.path.splitext(sys.argv[1])[1], ".asm") + '"') 
hash = open("a.out", "rb") 
hash = hash.read() 
hash = hex(zlib.crc32(hash)).replace("0x", "") 
if hash != file: 
    print(file) 
    print(hash)
