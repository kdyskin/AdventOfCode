text_file = open("input.txt", "r")
input = text_file.readlines()

def getSeatInfo(s):
    d = {}
    d["row"] = getRow(s[0:7])
    d["seat"] = getSeat(s[-3:])
    d["id"] = d["row"] * 8 + d["seat"]
    print(d)
    return d

def getRow(s):
    print(s)
    l = 0
    h = 127
    for c in s:
        if l<h:
            if c=="F":
                h = (h-1+l)/2
            else:
                l = (h+1+l)/2
        print(c + "->" + str(l) + " through " + str(h))
    return l

def getSeat(s):
    print(s)
    l = 0
    h = 7
    for c in s:
        if l<h:
            if c=="L":
                h = (h-1+l)/2
            else:
                l = (h+1+l)/2
        print(c + "->" + str(l) + " through " + str(h))
    return l

max = 0
ids = []
for line in input:
    d = getSeatInfo(line.strip())
    ids.append(d["id"])
    if d["id"]>max:
        max = d["id"]

ids.sort()
mySeat = 0
prevId = 83
for id in ids:
    if id-prevId>1:
        print(prevId+1)
    prevId = id
