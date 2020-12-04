# -*- coding: cp1252 -*-

import csv
import math

InputFile_name = "Day3Input.csv"

InputFile_h = open(InputFile_name,'r')
CSVInput = csv.reader(InputFile_h)

##next(CSVInput) #HEADER

numTrees = 0
xpos = 0
counter = 0
rows = sum(1 for line in CSVInput)

InputFile_h.seek(0)

first_line = next(CSVInput)
width = len(first_line[0])

print(rows)
print(width)

multiplier = math.ceil(rows / width)*4

print(multiplier)

InputFile_h.seek(0)

for record in CSVInput:
    counter+=1
    line = record[0]
    line = line * multiplier

    if counter == 1:
        xpos = 1
    else:
        xpos += 3

    if line[xpos-1] == ".":
        char = "O"
    else:
        char = "X"
        numTrees+=1

    newline = line[:xpos-1]+char+line[xpos:]

    print(str(counter) + "-" + newline)

print("NumberOfTrees: " + str(numTrees))

    


InputFile_h.close()


    
