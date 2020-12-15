text_file = open("input.txt", "r")
input = text_file.readlines()

answers = []
data = ""
count = 0
allYesCount = 0

for l in input:
    line = l.strip()
    print(line)
    if line == "":
        print("--->" + data)
        answers.append(data)
        data = ""
    else:
        if data != "":
            data += " "
        data += line

def createDictionary(s):
    dict = {"group_size":0}
    for a in s.split(" "):
        dict["group_size"] += 1
        for c in a:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
    print(dict)
    return dict

def getEveryonesYes(d):
    count = 0
    groupSize = d["group_size"]
    for value in d.values():
        if value == groupSize:
            count += 1
    print(str(groupSize) + "---->" + str(count-1) + "====>" + str(d))
    return count-1

for s in answers:
    d = createDictionary(s)
    #print(s + " ----> " + str(len(d)))
    count += len(d)-1
    allYesCount += getEveryonesYes(d)
print(count)
print(allYesCount)
