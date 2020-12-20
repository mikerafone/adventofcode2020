# -*- coding: cp1252 -*-

import re #regular expressions module
import math

InputFile_name = ".\Data\Day9Data.txt"

InputFile_h = open(InputFile_name,'r')

rawdata = InputFile_h.read()           #read the file
xmasRaw = rawdata.split("\n")   #split the file into individual boarding passes based on double new line
xmas = []

for x in xmasRaw:
    xmas.append(int(x))

workingset = xmas[:25]

#print(workingset)

def checkXmas(set,num):
    for s in set:
        remainder = num - s
        if remainder != s and remainder in set:
            return True

    return False

for i in xmas[25:]:
    result = checkXmas(workingset,i)

    if result == True:
        workingset.append(i)
        workingset.pop(0)
        #print(workingset)
    else:
        invalidNumber = i
        break

print(invalidNumber)


rangeposition = 0

def checkXmasPart2(rangepos):
    total = 0
    rangeNumbers = []
    for i in xmas[rangepos:]:
        total+= i
        rangeNumbers.append(i)
        if total == invalidNumber:
            print(rangeNumbers)
            weakness = min(rangeNumbers) + max(rangeNumbers)
            print(weakness)
            return
    rangepos += 1

    checkXmasPart2(rangepos)

checkXmasPart2(rangeposition)







InputFile_h.close()
