# -*- coding: cp1252 -*-

import re #regular expressions module

InputFile_name = ".\Data\Day7Data.txt"

InputFile_h = open(InputFile_name,'r')

rawdata = InputFile_h.read()           #read the file
rules = rawdata.split("\n")   #split the file into individual boarding passes based on double new line
ruleDict = dict()

for r in rules:
    bag = r[:r.find("bags contain")-1]
    contents = r[r.find("contain")+8:].replace(".","").split(", ")
    newcontents = []
    for c in contents:
        #print(c)
        new = re.search("(\d|no) (.*) bag*",c)
        newc = new.group(2)
        newcontents.append(newc)
    #print(bag)
    #print(contents)
    ruleDict[bag] = newcontents

#print(ruleDict)

baglist = []

for r in ruleDict:
    if "shiny gold" in ruleDict[r]:
        #print (ruleDict[r])
        baglist.append(r)

for bag in baglist:
    for r in ruleDict:
        if bag in ruleDict[r]:
            if r not in baglist:
                baglist.append(r)

#print(baglist)
print(str(len(baglist)))



InputFile_h.close()
