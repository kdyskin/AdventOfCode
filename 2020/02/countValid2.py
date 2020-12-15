
count = 0
text_file = open("input.txt", "r")
lines = text_file.readlines()
for i in range(0,len(lines)):
    line = lines[i].split(":")
    password = line[1].strip()
    policy = line[0].strip().split(" ")
    letter = policy[1]
    firstlast = policy[0].split("-")
    first = int(firstlast[0]) - 1
    last = int(firstlast[1]) - 1
    found = 0
    if password[first] == letter:
        found += 1
    if password[last] == letter:
        found += 1

    if found == 1:
        count += 1
        print("V -> " + str(first+1) + "-" + str(last+1) + " " + letter + " found " + str(found) + " in " + password)
    else:
        print("XXX -> " + str(first+1) + "-" + str(last+1) + " " + letter + " found " + str(found) + " in " + password)
    print(count)
print("Final count: " + str(count))

#    if
#print int(lines[0])+int(lines[1])
#print len(lines)
#text_file.close()
