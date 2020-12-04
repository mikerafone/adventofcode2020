# -*- coding: cp1252 -*-

import csv
import math

InputFile_name = "Day3Input.csv"

InputFile_h = open(InputFile_name,'r')
CSVInput = csv.reader(InputFile_h)

numTrees = 0
xpos = 0

rows = sum(1 for line in CSVInput)

InputFile_h.seek(0)

first_line = next(CSVInput)
width = len(first_line[0])

print(rows)
print(width)



## Right 1, Down 1
multiplier = math.ceil(rows / width)*1
print(multiplier)
InputFile_h.seek(0)
numtrees_1_1 = 0
counter = 0

for record in CSVInput:
    counter+=1
    line = record[0]
    line = line * multiplier

    if counter == 1:
        xpos = 1
    else:
        xpos += 1

    if line[xpos-1] == ".":
        char = "O"
    else:
        char = "X"
        numtrees_1_1 +=1

    newline = line[:xpos-1]+char+line[xpos:]

    #print(str(counter) + "-" + newline)

print("NumberOfTrees 1x1: " + str(numtrees_1_1))

## Right 3, Down 1
multiplier = math.ceil(rows / width)*4
print(multiplier)
InputFile_h.seek(0)
numtrees_3_1 = 0
counter = 0

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
        numtrees_3_1 +=1

    newline = line[:xpos-1]+char+line[xpos:]

    #print(str(counter) + "-" + newline)

print("NumberOfTrees 3x1: " + str(numtrees_3_1))

## Right 5, Down 1
multiplier = math.ceil(rows / width)*6
print(multiplier)
InputFile_h.seek(0)
numtrees_5_1 = 0
counter = 0

for record in CSVInput:
    counter+=1
    line = record[0]
    line = line * multiplier

    if counter == 1:
        xpos = 1
    else:
        xpos += 5

    if line[xpos-1] == ".":
        char = "O"
    else:
        char = "X"
        numtrees_5_1 +=1

    newline = line[:xpos-1]+char+line[xpos:]

    #print(str(counter) + "-" + newline)

print("NumberOfTrees 5x1: " + str(numtrees_5_1))

## Right 7, Down 1
multiplier = math.ceil(rows / width)*8
print(multiplier)
InputFile_h.seek(0)
numtrees_7_1 = 0
counter = 0

for record in CSVInput:
    counter+=1
    line = record[0]
    line = line * multiplier

    if counter == 1:
        xpos = 1
    else:
        xpos += 7

    if line[xpos-1] == ".":
        char = "O"
    else:
        char = "X"
        numtrees_7_1 +=1

    newline = line[:xpos-1]+char+line[xpos:]

    #print(str(counter) + "-" + newline)

print("NumberOfTrees 7x1: " + str(numtrees_7_1))

## Right 1, Down 2
multiplier = math.ceil(rows / width)*1
print(multiplier)
InputFile_h.seek(0)
numtrees_1_2 = 0
counter = 0

for record in CSVInput:
    counter+=1
    line = record[0]
    line = line * multiplier

    if counter == 1:
        xpos = 1
        newline = line[:xpos-1]+char+line[xpos:]
        ##print(str(counter) + "-" + newline)
    else:
        if counter % 2 == 1:
            xpos += 1
            if line[xpos-1] == ".":
                char = "O"
            else:
                char = "X"
                numtrees_1_2 +=1
            newline = line[:xpos-1]+char+line[xpos:]
            ##print(str(counter) + "-" + newline)
        ##else:
            ##print(str(counter) + "-" + line)

print("NumberOfTrees 1x2: " + str(numtrees_1_2))
    
totalTrees = numtrees_1_1 * numtrees_3_1 * numtrees_5_1 * numtrees_7_1 * numtrees_1_2

print ("Total Trees: " + str(totalTrees))

InputFile_h.close()


    
