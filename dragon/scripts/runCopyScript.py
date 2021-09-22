import sys
import os
import csv

#read list of libraries
f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()


#run copyScript for each library
for line in lines:
    os.system('python copyScript.py ' + "pincells/" + line.strip() + "/" + line.strip()  + "_pin_outTable.csv " + "assemblies/" + line.strip() + "/" + line.strip() + "_outTableFinal.csv")
