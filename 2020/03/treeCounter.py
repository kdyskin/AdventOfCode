count = 0
text_file = open("input.txt", "r")
lines = text_file.readlines()
j = 1
l = 0
for i in range(0,len(lines)):
    line = lines[i].strip()
    if i == 0 :
        l = len(line)
        print(l)
    else :
        j += 3
        if j > l:
            print(str(j) + "-> " + str(j % l))
            j = j % l
        print(line[j-1])
        if line[j-1] == "#":
            count += 1
print("Final count: " + str(count))
