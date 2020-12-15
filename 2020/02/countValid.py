
count = 0
text_file = open("input.txt", "r")
lines = text_file.readlines()
for i in range(0,len(lines)):
    line = lines[i].split(":")
    password = line[1].strip()
    policy = line[0].strip().split(" ")
    letter = policy[1]
    minmax = policy[0].split("-")
    min = int(minmax[0])
    max = int(minmax[1])
    found = password.count(letter)
    if found in range(min, max+1):
        count += 1
        print("V -> " + str(min) + "-" + str(max) + " " + letter + " found " + str(found) + " in " + password)
    else:
        print("XXX -> " + str(min) + "-" + str(max) + " " + letter + " found " + str(found) + " in " + password)
    print(count)
print("Final count: " + str(count))
#    if
#print int(lines[0])+int(lines[1])
#print len(lines)
#text_file.close()
