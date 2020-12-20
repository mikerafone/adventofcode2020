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

def processComponent(instructionset,component,acc):
    #print(component)
    if len(component) > 3:
        #print("looped with acc of "+ str(acc))
        return    
    
    recordNo = component[0]

    instructionset[recordNo].append("Y")

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
    
    if recordNo > 650:
        print("finished successfully with acc of "+ str(acc))
        return

    processComponent(instructionset,instructionset[recordNo],acc)
    
    #return(value)

processComponent(instructions,instructions[recordNo],accumulator)

for r in instructions:
    revisedinstructions = []
    counter = 0
    for i in instructionsRaw:
        components = i.split(" ")
        components.insert(0,counter)
        counter +=1
        # print(components)
        revisedinstructions.append(components)


    recordNo = 0
    accumulator = 0
    recordNum = r[0]
    op = r[1]
    accum = r[2]
    if op == "jmp":
        revisedinstructions[recordNum][1] = "nop"
    elif op == "nop":
        revisedinstructions[recordNum][1] = "jmp"
    
    processComponent(revisedinstructions,revisedinstructions[recordNo],accumulator)

InputFile_h.close()
