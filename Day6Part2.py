# -*- coding: cp1252 -*-

import re #regular expressions module

InputFile_name = ".\Data\Day6Data.txt"

InputFile_h = open(InputFile_name,'r')

rawdata = InputFile_h.read()           #read the file
groups = rawdata.split("\n\n")   #split the file into individual boarding passes based on double new line
totalQuestions = 0

for g in groups:
    person = g.split("\n")
    person1answers = person[0]
    numQuestions = 0
    for a in person1answers:
        numOcc = 0
        for p in person:
            if a in p:
                numOcc +=1
        if numOcc == len(person):
            numQuestions +=1
    totalQuestions += numQuestions

print(str(totalQuestions))

InputFile_h.close()
