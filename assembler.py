import os
import pathlib
file = input("File to disassemble: ")

if os.path.isfile(file):
    print("")
else:
    raise Exception("File not found!")

linesWritten = 0
fileoutput = file.split(".")
fileoutput = fileoutput[0]
fileoutput = fileoutput + ".asm"
fileoutput = open(fileoutput, "w")

for byte in pathlib.Path(file).read_bytes():
    if byte >= 16:
        hexVersion = hex(byte)
    else:
        hexVersion = "0" + hex(byte)
    hexVersion = hexVersion.replace("0x", "")
    instruction = ".DB $" + hexVersion
    if linesWritten == 0:
        fileoutput.write(instruction)
        linesWritten += 1
    else:
        fileoutput.write("\n" + instruction)
os.remove(file)
fileoutput.close()
file = input("File to assemble: ")
fileinput = open(file)

if os.path.isfile(file) and ".asm" in file:
    print("")
else:
    raise Exception("File not found!")

linesWritten = 0

bytesArr = [B'\x00', B'\x01', B'\x02', B'\x03', B'\x04', B'\x05', B'\x06', B'\x07', B'\x08', B'\x09', B'\x0A', B'\x0B', B'\x0C', B'\x0D', B'\x0E', B'\x0F', B'\x10', B'\x11', B'\x12', B'\x13', B'\x14', B'\x15', B'\x16', B'\x17', B'\x18', B'\x19', B'\x1A', B'\x1B', B'\x1C', B'\x1D', B'\x1E', B'\x1F', B'\x20', B'\x21', B'\x22', B'\x23', B'\x24', B'\x25', B'\x26', B'\x27', B'\x28', B'\x29', B'\x2A', B'\x2B', B'\x2C', B'\x2D', B'\x2E', B'\x2F', B'\x30', B'\x31', B'\x32', B'\x33', B'\x34', B'\x35', B'\x36', B'\x37', B'\x38', B'\x39', B'\x3A', B'\x3B', B'\x3C', B'\x3D', B'\x3E', B'\x3F', B'\x40', B'\x41', B'\x42', B'\x43', B'\x44', B'\x45', B'\x46', B'\x47', B'\x48', B'\x49', B'\x4A', B'\x4B', B'\x4C', B'\x4D', B'\x4E', B'\x4F', B'\x50', B'\x51', B'\x52', B'\x53', B'\x54', B'\x55', B'\x56', B'\x57', B'\x58', B'\x59', B'\x5A', B'\x5B', B'\x5C', B'\x5D', B'\x5E', B'\x5F', B'\x60', B'\x61', B'\x62', B'\x63', B'\x64', B'\x65', B'\x66', B'\x67', B'\x68', B'\x69', B'\x6A', B'\x6B', B'\x6C', B'\x6D', B'\x6E', B'\x6F', B'\x70', B'\x71', B'\x72', B'\x73', B'\x74', B'\x75', B'\x76', B'\x77', B'\x78', B'\x79', B'\x7A', B'\x7B', B'\x7C', B'\x7D', B'\x7E', B'\x7F', B'\x80', B'\x81', B'\x82', B'\x83', B'\x84', B'\x85', B'\x86', B'\x87', B'\x88', B'\x89', B'\x8A', B'\x8B', B'\x8C', B'\x8D', B'\x8E', B'\x8F', B'\x90', B'\x91', B'\x92', B'\x93', B'\x94', B'\x95', B'\x96', B'\x97', B'\x98', B'\x99', B'\x9A', B'\x9B', B'\x9C', B'\x9D', B'\x9E', B'\x9F', B'\xA0', B'\xA1', B'\xA2', B'\xA3', B'\xA4', B'\xA5', B'\xA6', B'\xA7', B'\xA8', B'\xA9', B'\xAA', B'\xAB', B'\xAC', B'\xAD', B'\xAE', B'\xAF', B'\xB0', B'\xB1', B'\xB2', B'\xB3', B'\xB4', B'\xB5', B'\xB6', B'\xB7', B'\xB8', B'\xB9', B'\xBA', B'\xBB', B'\xBC', B'\xBD', B'\xBE', B'\xBF', B'\xC0', B'\xC1', B'\xC2', B'\xC3', B'\xC4', B'\xC5', B'\xC6', B'\xC7', B'\xC8', B'\xC9', B'\xCA', B'\xCB', B'\xCC', B'\xCD', B'\xCE', B'\xCF', B'\xD0', B'\xD1', B'\xD2', B'\xD3', B'\xD4', B'\xD5', B'\xD6', B'\xD7', B'\xD8', B'\xD9', B'\xDA', B'\xDB', B'\xDC', B'\xDD', B'\xDE', B'\xDF', B'\xE0', B'\xE1', B'\xE2', B'\xE3', B'\xE4', B'\xE5', B'\xE6', B'\xE7', B'\xE8', B'\xE9', B'\xEA', B'\xEB', B'\xEC', B'\xED', B'\xEE', B'\xEF', B'\xF0', B'\xF1', B'\xF2', B'\xF3', B'\xF4', B'\xF5', B'\xF6', B'\xF7', B'\xF8', B'\xF9', B'\xFA', B'\xFB', B'\xFC', B'\xFD', B'\xFE', B'\xFF']

fileFormat = input("File format of binary: ")
fileoutput = open(file.replace(".asm", fileFormat), "wb")

while True:
    line = fileinput.readline()
    if not line:
        break
    line = line.split(".")
    line = line[1]
    line = line.replace("\n", "")
    line = "." + line
    if line.isspace() == False:
        if ".DB $" not in line:
            raise Exception(".DB $ must be in any line that is not whitespace!")
        if len(line.replace(".DB $", "")) == 2:
            line = line.replace(".DB $", "")
            line = int(line, 16)
            line = bytesArr[line]
            fileoutput.write(line)
        else:
            raise Exception("Character length of hex number must be 2!")
fileoutput.close()