# -*- coding: cp1252 -*-

import re #regular expressions module
import math

InputFile_name = ".\Data\Day7Data.txt"

InputFile_h = open(InputFile_name,'r')

rawdata = InputFile_h.read()           #read the file
rules = rawdata.split("\n")   #split the file into individual boarding passes based on double new line
ruleDict = dict()

totalbags = 0

def findBags(bagColour):
    numbags = 0
    for content in ruleDict[bagColour]:
        print(content)
        if content["num"] != 0:
            numbags += int(content["num"])
            numbags += content["num"]*findBags(content["colour"])
    return numbags
    

for r in rules:
    bag = r[:r.find("bags contain")-1]
    contents = r[r.find("contain")+8:].replace(".","").split(", ")
    newcontents = []
    for c in contents:
        contentDict = dict()
        #print(c)
        if c != "no other bags":
            newc = re.search("(\d) (.*) bag*",c)
            num = int(newc.group(1))
            colour = newc.group(2)
            # print(num)
            # print(colour)
        else:
            num = 0
            colour = "no other bags"

        contentDict["num"] = num
        contentDict["colour"] = colour

        newcontents.append(contentDict)
    #print(bag)
    #print(contents)
    ruleDict[bag] = newcontents

#print(ruleDict)

for content in ruleDict["shiny gold"]:
    print(content["num"])
    print(content["colour"])



totalbags += findBags("shiny gold")

print(totalbags)




# baglist = []

# for r in ruleDict:
#     if "shiny gold" in ruleDict[r]:
#         #print (ruleDict[r])
#         baglist.append(r)

# for bag in baglist:
#     for r in ruleDict:
#         if bag in ruleDict[r]:
#             if r not in baglist:
#                 baglist.append(r)

# #print(baglist)
# print(str(len(baglist)))



InputFile_h.close()
