import sys
import os
import dragonScript1KEFF
import csv

#Script implementing dragonScript1KEFF.py on a file of inputs and outputting a csv file

f = open(sys.argv[1], "r")
list_of_lines = f.readlines()
f.close()

header = ['CaseName','Fuel Temperature','Moderator Temperature', 'Moderator Density', 'Library','Theoretical Keff', 'Simulated Keff', 'error in PCM']

# create list to fill
data = []
output = []       
#fill it line by line
for line in list_of_lines:
     output = dragonScript1KEFF.main(str(line.split()[1]), str(line.split()[2]), str(line.split()[3]), str(line.split()[4]), str(line.split()[5]))
     output.insert(0, str(line.split()[0]))
     data.append(output)

with open(sys.argv[2], 'w+') as f1:
    writer = csv.writer(f1, delimiter=",",lineterminator="\n")

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
