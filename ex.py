
import os
import csv
from collections import defaultdict


files = open("tes.csv",encoding='utf-8') ## Open CSV File
reader = csv.DictReader(files,delimiter=';') ## Read CSV File with Delimiter

ArrEmail = [] ## Set Array Email
ArrTelephone = [] ## Set Array Telephone

for row in reader: ## Looping for Get Data By Row
    infoEmail = [row['Name'],row['Email']]
    infoTelephone = [row['Name'],row['Telephone']]
    ArrEmail.append(infoEmail)
    ArrTelephone.append(infoTelephone)

def combine(data): ## Function to Combine All Data by Column Name
    ex = defaultdict(list)
    for src, *sel in data:
        if not ex:
            ex[src] += sel
        else:
            ex[src] += sel
    return ex

## Call Function Extract
dictEmail = combine(ArrEmail)
dictTelephone = combine(ArrTelephone)
for name in dictEmail: ## Looping for Remove Duplicate by Columns Name

    ## Function To Remove Duplicate
    dupEmail = list(dict.fromkeys(dictEmail[name])) 
    valueEmail = ', '.join(dupEmail)

    dupTelephone = list(dict.fromkeys(dictTelephone[name]))
    valueTelephone = ', '.join(dupTelephone)

    print("-----------"+name+"-----------\n")
    print(" Email : "+valueEmail+"\n")
    print(" Telephone : "+valueTelephone+"\n\n")