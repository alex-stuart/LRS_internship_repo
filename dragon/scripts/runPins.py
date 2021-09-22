import sys
import os
import csv

#read list of libraries
f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

#read list of assemblies
ASSBLYS = open("inputFile.txt", "r")
ASSBLYS_lines = ASSBLYS.readlines()
ASSBLYS.close()
 

#runMultKEFFfile for each library
for line in lines:
     #modify list of assemblies 
     ASSBLYS_lines1 = []
     for ASSBLYS_line in ASSBLYS_lines:
          columns = ASSBLYS_line.split(" ")
	  columns[4] = str(line).strip()
          ASSBLYS_line = " ".join(columns)
          ASSBLYS_lines1.append(ASSBLYS_line)
     ASSBLYS = open("inputFile.txt", "w")
     ASSBLYS.writelines(ASSBLYS_lines1)
     ASSBLYS.close()

     #create outputFile
     outFile = str(line)[:len(line) - 1]  + '_pin_outTable.csv '
     #runMultKEFFfile
     os.system('python dragonScriptKEFFfile.py inputFile.txt ' + outFile )  
