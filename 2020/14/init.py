def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    input = []
    for line in lines:
        com = {}
        i = line.strip().split(" = ")
        com["command"] = i[0]
        com["val"] = i[1]
        input.append(com)
    text_file.close()
    return input

def decToBin(num):
    s = str(num%2)
    if num > 1:
        s += decToBin(num // 2)
    return s

def valTo36(num):
    s = ""
    bNum = decToBin(num)
    for i in range(36):
        if i<len(bNum):
            s = bNum[i] + s
        else:
            s = "0" + s
    return s

def valToDec(val):
    i = 0
    for c in val:
        if c=="0":
            i += 1
        else:
            break
    #print(val,end=" ")
    return int(val[i:], 2)

def applyMask(val,mask):
    s = ""
    for i in range(len(mask)):
        if mask[i]=="X":
            s = s + val[i]
        else:
            s = s + mask[i]
    return s

def main():
    input = readInput()
    #print(input)
    mem = {}
    mask = ""
    #print(valToDec(valTo36(73)))
    #print(applyMask("000000000000000000000000000001100101","XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"))
    for com in input:
        if com["command"] == "mask":
            mask = com["val"]
        else:
            mem[com["command"]] = valToDec(applyMask(valTo36(int(com["val"])),mask))
    sum = 0
    for key in mem:
        sum += mem[key]
    print(sum)

if __name__ == "__main__":
    main()
