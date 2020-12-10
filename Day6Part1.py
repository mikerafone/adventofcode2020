# -*- coding: cp1252 -*-

import re #regular expressions module

InputFile_name = ".\Data\Day6Data.txt"

InputFile_h = open(InputFile_name,'r')

rawdata = InputFile_h.read()           #read the file
groups = rawdata.split("\n\n")   #split the file into individual boarding passes based on double new line
totalQuestions = 0

for g in groups:
    g = g.replace("\n","")
    distinctQuestions = ''.join(set(g))
    #print(g)
    #print(distinctQuestions)
    totalQuestions += len(distinctQuestions)

print(str(totalQuestions))

InputFile_h.close()

    


