text_file = open("input.txt", "r")
input = text_file.readlines()

def c(r, d, lines):
    count = 0
    j = 1
    l = 0
    for i in range(0,len(lines),d):
        line = lines[i].strip()
        if i == 0 :
            l = len(line)
        else :
            j += r
            if j > l:
                j = j % l
            if line[j-1] == "#":
                count += 1
    return count

print(str(c(1, 1, input)*c(3, 1, input)*c(5, 1, input)*c(7, 1, input)*c(1, 2, input)))
