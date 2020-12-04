# -*- coding: cp1252 -*-

import re #regular expressions module

InputFile_name = "Day4Input.txt"

InputFile_h = open(InputFile_name,'r')

passportsRaw = InputFile_h.read()           #read the file
passportList = passportsRaw.split("\n\n")   #split the file into individual passports based on double new line
passportListOfDicts = [dict()]


validPassports = 0

#print(passportList)

for p in passportList:
    p = p.replace("\n"," ")                 #replace new lines inside each passport so they're separated only by spaces

    #print(p)
    passportDict = dict()

    for i in p.split(" "):                  #iterate through each field in each passport
        colonPosition = i.find(":")         #find the position of the colon in each field
        #print(colonPosition)
        passportDict[i[:colonPosition]] = i[colonPosition+1:]   #for each field, get the part before the colon to use as the key in dict, and the part after to store as the value
        #print(passportDict)

    passportListOfDicts.append(passportDict)    #add the dictionary for the passport to the overall list

#print(passportListOfDicts)

for x in passportListOfDicts:           #iterate through the passports in dict form
    #print(len(x))

    if all (k in x for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):       #if the passport you're looking at has all the fields except the cid which is optional
        byr = int(x["byr"])         
        iyr = int(x["iyr"])
        eyr = int(x["eyr"])                                                     #assign variables
        hgt = x["hgt"]
        hgt_unit = hgt[-2:]                                                     #split hgt into unit and value
        hgt_value = hgt[:-2]
        hcl = x["hcl"]
        ecl = x["ecl"]
        pid = x["pid"]

        #print(hgt)
        #print(hgt_unit)
        #print(hgt_value)

        if 1920 <= byr <= 2002:                                                                 #check if dates are inside valid ranges
            if 2010 <= iyr <= 2020:
                if 2020 <= eyr <= 2030:
                    if re.search(r"^#[0-9a-f]{6}$", hcl) != None:                               #check if hcl matches regex for # + 6 numbers / letters
                        if ecl in ("amb","blu","brn","gry","grn","hzl","oth"):                  #check if ecl is in defined list
                            if re.search(r"^[0-9]{9}$", pid) != None:
                                if hgt_unit == "cm":                                            #do hgt last as it has 2 possible outcomes depending on the unit
                                    if 150 <= int(hgt_value) <= 193:
                                        validPassports +=1
                                elif hgt_unit == "in":
                                    if 59 <= int(hgt_value) <= 76:
                                        validPassports +=1
                                        


print("Valid Passports: " + str(validPassports))

InputFile_h.close()


    
