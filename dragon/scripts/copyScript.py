import sys
import os

f = open("PCMresultsTableFinal.csv", "r")
lines = f.readlines()
f.close()

pinFile = open(sys.argv[1], "r")
pinLines = pinFile.readlines()
pinFile.close()

assblyFile = open(sys.argv[2], "r")
assblyLines = assblyFile.readlines()
assblyFile.close()

for i in range(1, len(pinLines)):
    lines[i]=lines[i].strip() + ", " + pinLines[i].split(",")[7] #+ "\n"

for i in range(1, len(assblyLines)):
    lines[i+4]=lines[i+4].strip() + ", " + assblyLines[i].split(",")[9] #+ "\n"

#lines[5]=lines[5].strip() + ", " + assblyLines[1].split(",")[9] #+ "\n"

f = open("PCMresultsTableFinal.csv", "w")
f.writelines(lines)
f.close()
