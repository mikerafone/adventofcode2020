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

def workOutTrees(x,y): ##only works for 1 down at a time, didn't use this in the end
    print(str(x)+ " across and " + str(y) + " down")

    multiplier = math.ceil(rows / width) * x
    #print(multiplier)
    numtrees = 0
    counter = 0
    
    InputFile_h.seek(0)
    for record in CSVInput:
        counter+=1
        line = record[0]
        line = line * multiplier

        if counter == 1:
            xpos = 1
        else:
            
            xpos += x

        if line[xpos-1] == ".":
            char = "O"
        else:
            char = "X"
            numtrees +=1

        newline = line[:xpos-1]+char+line[xpos:]

        #print(str(counter) + "-" + newline)

    print("NumberOfTrees "+str(x)+"x"+str(y)+": " + str(numtrees))
    return numtrees

def workOutTreesOffset(x,y):
    print(str(x)+ " across and " + str(y) + " down")

    multiplier = math.ceil(rows / width) * x
    #print(multiplier)
    numtrees = 0
    counter = 0
    offsetcounter = 1
    
    InputFile_h.seek(0)
    for record in CSVInput:
        counter+=1
        
        line = record[0]
        line = line * multiplier

        if counter == 1:
            xpos = 1
            if counter == offsetcounter:
                offsetcounter+= y
        else:
           ##print(str(counter) + "-"+str(offsetcounter))
           if counter == offsetcounter:
            offsetcounter+= y
            xpos += x
            if line[xpos-1] == ".":
                char = "O"
            else:
                char = "X"
                numtrees +=1
            newline = line[:xpos-1]+char+line[xpos:]
        #print(str(counter) + "-" + newline)

    print("NumberOfTrees (offset) "+str(x)+"x"+str(y)+": " + str(numtrees))
    return numtrees

##workOutTrees(1,1)
##workOutTreesOffset(1,1)
##workOutTrees(3,1)
##workOutTreesOffset(3,1)
##workOutTrees(5,1)
##workOutTreesOffset(5,1)
##workOutTrees(7,1)
##workOutTreesOffset(7,1)
##workOutTreesOffset(1,2) 
    
totalTrees = workOutTreesOffset(1,1) * workOutTreesOffset(3,1) * workOutTreesOffset(5,1) * workOutTreesOffset(7,1) * workOutTreesOffset(1,2)

print ("Total Trees: " + str(totalTrees))

InputFile_h.close()


    
