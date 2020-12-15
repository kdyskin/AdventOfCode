def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    input = {}
    time = int(lines[0])
    buses = []
    for bus in lines[1].split(","):
        if bus != "x":
            buses.append(int(bus))
    text_file.close()
    input["time"] = time
    input["buses"] = buses
    return input

def main():
    dict = readInput()
    print(dict)
    nextArrival = []
    for bus in dict["buses"]:
        nextArrival.append(bus-dict["time"]%bus)
    print(dict)
    i = nextArrival.index(min(nextArrival))
    print("Answer to 1 is %d"%(nextArrival[i]*dict["buses"][i]))

if __name__ == "__main__":
    main()
