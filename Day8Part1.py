# -*- coding: cp1252 -*-

import re #regular expressions module
import math

InputFile_name = ".\Data\Day8Data.txt"

InputFile_h = open(InputFile_name,'r')

rawdata = InputFile_h.read()           #read the file
instructionsRaw = rawdata.split("\n")   #split the file into individual boarding passes based on double new line
instructions = []
accumulator = 0
counter = 0
recordNo = 0
maxRecordNo = 0

for i in instructionsRaw:
    components = i.split(" ")
    components.insert(0,counter)
    counter +=1
    # print(components)
    instructions.append(components)

def processComponent(component,acc):
    #print(component)
    if len(component) > 3:
        print(acc)
        return    
    
    recordNo = component[0]

    instructions[recordNo].append("Y")

    operation = component[1]
    value = int(component[2])
    
    if operation == "jmp":
        recordNo += value
    if operation == "acc":
        #print(accumulator)
        #print(value)
        acc += value
        recordNo += 1
    if operation == "nop":
        recordNo += 1

    processComponent(instructions[recordNo],acc)
    
    #return(value)

processComponent(instructions[recordNo],accumulator)

InputFile_h.close()
