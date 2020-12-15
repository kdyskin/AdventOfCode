import re

text_file = open("input.txt", "r")
lines = text_file.readlines()

def createDictionary(s):
    d = {}
    input = s.split(" ")
    for i in input:
        pair = i.split(":")
        d[pair[0]] = pair[1]
    return d

data = ""
batch = []
validKeysBatch = []
validValuesBatch = []
for l in lines:
    line = l.strip()
    if line == "":
        #print(data)
        d = createDictionary(data)
        #print(d)
        batch.append(d)
        data = ""
    else:
        if data != "":
            data += " "
        data += line

def checkKeys(keys, dict):
    for key in keys:
        if key not in dict.keys():
            return False
    return True

def checkValues(dict):
    byr = int(dict['byr'])
    if byr < 1920 or byr > 2002:
        return False
    iyr = int(dict['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    eyr = int(dict['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', dict['hcl']):
        #print("Invalid HCL: " + dict['hcl'])
        return False
    if not re.search(r'^(\d{9})$', dict['pid']):
        #print("Invalid PID: " + dict['pid'])
        return False
    if dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if dict['hgt'].endswith("in"):
        v = int(dict['hgt'][0:-2])
        if v < 59 or v > 76:
            print("Invalid HGT: " + dict['hgt'])
            return False
    if dict['hgt'].endswith("cm"):
        v = int(dict['hgt'][0:-2])
        if v < 150 or v > 193:
            print("Invalid HGT: " + dict['hgt'])
            return False
    return True
k = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
#cid

for d in batch:
    if checkKeys(k,d):
        #print("VALID: " + str(d))
        validKeysBatch.append(d)
    #else:
        #print("INVALID: " + str(d))

for d in validKeysBatch:
    if checkValues(d):
        print("VALID YEAR: " + str(d))
        validValuesBatch.append(d)
#print(count)
print(len(validValuesBatch))
#print(str(c(1, 1, input)*c(3, 1, input)*c(5, 1, input)*c(7, 1, input)*c(1, 2, input)))
