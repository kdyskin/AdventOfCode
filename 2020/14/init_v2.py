def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    input = []
    for line in lines:
        com = {}
        i = line.strip().split(" = ")
        if i[0] == "mask":
            com["command"] = i[0]
        else:
            com["command"] = int(i[0][4:-1])
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
        if mask[i]=="0":
            s = s + val[i]
        else:
            s = s + mask[i]
    return s

def getAddresses(valList):
    addresses = []
    rec = False
    for address in valList:
        try:
            i = address.index("X")
            addresses.append(address[:i] + "0" + address[i+1:])
            addresses.append(address[:i] + "1" + address[i+1:])
            rec = True
        except ValueError as e:
            addresses.append(address)
    if rec:
        return getAddresses(addresses)
    return addresses

def main():
    input = readInput()
    mem = {}
    mask = ""
    for com in input:
        if com["command"] == "mask":
            mask = com["val"]
        else:
            for addr in getAddresses([applyMask(valTo36(com["command"]),mask)]):
                mem[valToDec(addr)] = int(com["val"])
    sum = 0
    for key in mem:
        sum += mem[key]
    print(sum)

if __name__ == "__main__":
    main()
