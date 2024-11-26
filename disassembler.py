import os 
import sys 
import pathlib 
import zlib
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
start = 65536 - os.path.getsize(sys.argv[1])
while fileBytes < len(bytesArr):
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
                        highByte = hex(start + fileBytes + 1 - (255 - highByte)).replace("0x", "") 
                    else: 
                        highByte = hex(start + fileBytes + highByte + 2).replace("0x", "") 
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
    if linesWritten == False:
        fileoutput.write(instruction) 
        linesWritten = True
    else:
        fileoutput.write("\n" + instruction) 
    fileBytes += 1 
fileoutput.close() 
os.system('python assembler.py ' + hex(start).replace("0x", "") + ' "' + sys.argv[1].replace(os.path.splitext(sys.argv[1])[1], ".asm") + '"') 
hash = open("a.out", "rb") 
hash = hash.read() 
hash = hex(zlib.crc32(hash)).replace("0x", "") 
if hash != file: 
    print(file) 
    print(hash)