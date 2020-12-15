text_file = open("input.txt", "r")
input = text_file.readlines()

def parseInput(lines):
    rules = []
    for line in lines:
        d = {}
        l = line.strip().split(" bags contain ")
        d["bag"] = l[0]
        if l[1] != "no other bags.":
            d = parseContents(d,l[1])
        rules.append(d)
    return rules

def parseContents(d,s):
    s = s.replace(" bags.","").replace(" bag.","").replace(" bags","").replace(" bag","")
    tokens = s.split(", ")
    for token in tokens:
        d[token[2:]] = int(token[0])
    return d

rules = parseInput(input)

def getAllBagTypes(bags,color):
    #start by identifying all bags that can hold 'color'
    for rule in rules:
        if color in rule.keys():
            #add bag in this rule
            if rule["bag"] in bags:
                print(rule["bag"] + " already counted")
            else:
                bags.append(rule["bag"])
            print(color + " can be in " + rule["bag"])
            #recursively find all bag types where bag in this rule can be
            bags = getAllBagTypes(bags,rule["bag"])
    return bags

def findInRules(color):
    for rule in rules:
        if rule["bag"] == color:
            return rule

def howManyBagsInside(color):
    count = 1
    d = findInRules(color)
    print("Examining :" + str(d))
    #if cannot have any other bags inside
    if len(d) == 1:
        print(color + " cannot have any other bags inside")
        return 1
    else:
        for key in d.keys():
            if key != "bag":
                count += d[key] * howManyBagsInside(key)
    print(color + " can have " + str(count) + " other bags inside")
    return count

#for question 1 uncomment the following 2 lines
#bagTypes = getAllBagTypes([],"shiny gold")
#print(len(bagTypes))

#for question 2, below is including main bag, so answer is what howManyBagsInside function returns minus 1
print(howManyBagsInside("shiny gold")-1)
