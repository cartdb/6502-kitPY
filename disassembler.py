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
