class Ferry:
    mDistance = {"x" : 0, "y" : 0}

    def move(self,instruction):
        d = self.directionFacing
        if instruction["command"] != "F":
            d = instruction["command"]
        if d=="N":
            self.mDistance["y"] += instruction["val"]
        if d=="S":
            self.mDistance["y"] -= instruction["val"]
        if d=="E":
            self.mDistance["x"] += instruction["val"]
        if d=="W":
            self.mDistance["x"] -= instruction["val"]
        print("Moved %d units %s"%(instruction["val"],d))
        print("Current distance traveled: " + str(self.mDistance))

    def turn(self,instruction):
        directions = ["N","E","S","W"]
        ticks = int(instruction["val"]/90)
        if instruction["command"] == "L":
            ticks *= -1
        di = directions.index(self.directionFacing)
        self.directionFacing = directions[(di+ticks)%4]
        print("Turned " + instruction["command"] + "%d degrees (%d ticks)."%(instruction["val"],ticks))
        print("Direction facing now: " + self.directionFacing)

    def action(self, instruction):
        print("Actioning: " + str(instruction))
        if instruction["command"]=="L" or instruction["command"]=="R":
            self.turn(instruction)
        else:
            self.move(instruction)

    def getManhattanDistance(self):
        return abs(self.mDistance["x"]) + abs(self.mDistance["y"])
        
    def __init__(self, d):
        self.directionFacing = d

def readInput():
    text_file = open("input1.txt", "r")
    lines = text_file.readlines()
    #start with 0 -> charging outlet
    input = []
    for line in lines:
        inst = {}
        i = line.strip()
        inst["command"] = i[0]
        inst["val"] = int(i[1:])
        input.append(inst)
    text_file.close()
    return input

def main():
    ferry = Ferry("E")
    print(ferry.mDistance)
    instructions = readInput()
    for instruction in instructions:
        ferry.action(instruction)
    print(ferry.getManhattanDistance())

if __name__ == "__main__":
    main()
