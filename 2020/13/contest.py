def readInput():
    text_file = open("input1.txt", "r")
    lines = text_file.readlines()
    list = lines[1].split(",")
    input = []
    for i in range(len(list)):
        if list[i] == "x":
            continue
        dict = {}
        dict["id"] = int(list[i])
        dict["offset"] = i
        input.append(dict)
    text_file.close()
    return input

def main():
    buses = readInput()
    t = buses[0]["id"]
    incr = t
    i = 1
    while i<len(buses):
        t += incr
        if (t+buses[i]["offset"])%buses[i]["id"] == 0:
            print(t)
            incr *= buses[i]["id"]
            i += 1

if __name__ == "__main__":
    main()
