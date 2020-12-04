# -*- coding: cp1252 -*-

import csv
import math

InputFile_name = "Day4Input.txt"

InputFile_h = open(InputFile_name,'r')

passportsRaw = InputFile_h.read()
passportList = passportsRaw.split("\n\n")
passportListOfDicts = [dict()]


validPassports = 0

#print(passportList)

for p in passportList:
    p = p.replace("\n"," ")

    #print(p)
    passportDict = dict()

    for i in p.split(" "):
        colonPosition = i.find(":")
        #print(colonPosition)
        passportDict[i[:colonPosition]] = i[colonPosition+1:]
        #print(passportDict)

    passportListOfDicts.append(passportDict)

#print(passportListOfDicts)

for x in passportListOfDicts:
    #print(len(x))

    if all (k in x for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):
        validPassports +=1

print("Valid Passports: " + str(validPassports))
    
InputFile_h.close()


    
