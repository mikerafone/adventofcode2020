# -*- coding: cp1252 -*-

import csv

InputFile_name = "Day2Part1Data.csv"

InputFile_h = open(InputFile_name,'r')
CSVInput = csv.reader(InputFile_h)

next(CSVInput) #HEADER

valid_pw = 0

for record in CSVInput:
    min_occ = int(record[0].strip())
    max_occ = int(record[1].strip())
    letter = record[2].strip()
    password = record[3].strip()

    occ = 0

    for l in password:
        if l == letter:
            occ += 1

    if occ >= min_occ and occ <= max_occ:
        valid_pw += 1


print (valid_pw)

InputFile_h.close()


    
