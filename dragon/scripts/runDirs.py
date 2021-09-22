import sys
import os
import csv

#read list of libraries
f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

#read list of assemblies
ASSBLYS = open("inputASSBLYFile1.txt", "r")
ASSBLYS_lines = ASSBLYS.readlines()
ASSBLYS.close()
 

#runMultKEFFfile for each library
for line in lines:
     #modify list of assemblies 
     ASSBLYS_lines1 = []
     for ASSBLYS_line in ASSBLYS_lines:
          columns = ASSBLYS_line.split(" ")
	  columns[5] = str(line).strip()
          ASSBLYS_line = " ".join(columns)
          ASSBLYS_lines1.append(ASSBLYS_line)
     ASSBLYS = open("inputASSBLYFile1.txt", "w")
     ASSBLYS.writelines(ASSBLYS_lines1)
     ASSBLYS.close()

     #create outputFile
     outFile = str(line)[:len(line) - 1]  + '_outTableFinal.csv '
     #runMultKEFFfile
     os.system('python MultKEFFfile.py inputASSBLYFile1.txt ' + outFile )  
