# -*- coding: cp1252 -*-

import re #regular expressions module

InputFile_name = ".\Data\Day5Data.txt"

InputFile_h = open(InputFile_name,'r')

bpassRaw = InputFile_h.read()           #read the file
bpassList = bpassRaw.split("\n")   #split the file into individual boarding passes based on double new line
bpassIds = []

def returnHalf(values,char):
    halfway = len(values)/2
    #print(halfway)
    if char in ("F","L"):
        return values[:int(halfway)]
    elif char in ("B","R"):
        return values[int(halfway):]

for p in bpassList:
    rowArray = []
    seatArray = []
    for a in range(0,128):
        rowArray.append(a)
    #print(rowArray)
    for b in range(0,8):
        seatArray.append(b)
    row = p[:7]
    seat = p[7:]
    #print(row)
    #print(seat)

    for r in row:
        rowArray = returnHalf(rowArray,r)
    for s in seat:
        seatArray = returnHalf(seatArray,s)
    
    rowNo = rowArray[0]
    seatNo = seatArray[0]

    seatId = rowNo * 8 + seatNo 

    #print(str(rowNo)+ "-"+str(seatNo)+"-"+str(seatId))
    bpassIds.append(seatId)

print(max(bpassIds))
    

    


