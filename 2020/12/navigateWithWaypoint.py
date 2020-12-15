class Ferry:
    mDistance = {"x" : 0, "y" : 0}

    def forward(self,instruction):
        self.mDistance["x"] = self.mDistance["x"] + self.waypoint["x"]*instruction["val"]
        self.mDistance["y"] = self.mDistance["y"] + self.waypoint["y"]*instruction["val"]
        print("Current position is: " + str(self.mDistance))

    def move(self,instruction):
        if instruction["command"]=="N":
            self.waypoint["y"] += instruction["val"]
        if instruction["command"]=="S":
            self.waypoint["y"] -= instruction["val"]
        if instruction["command"]=="E":
            self.waypoint["x"] += instruction["val"]
        if instruction["command"]=="W":
            self.waypoint["x"] -= instruction["val"]
        print("Moved waypoint %d units %s"%(instruction["val"],instruction["command"]))
        print("Current waypoint: " + str(self.waypoint))

    def turn(self,instruction):
        directions = ["N","E","S","W"]
        ticks = int(instruction["val"]/90)%4
        x = self.waypoint["x"]
        y = self.waypoint["y"]
        if instruction["command"] == "R":
            if ticks==1:
                self.waypoint["x"] = y
                self.waypoint["y"] = -x
            if ticks==2:
                self.waypoint["x"] = -x
                self.waypoint["y"] = -y
            if ticks==3:
                self.waypoint["x"] = -y
                self.waypoint["y"] = x
        if instruction["command"] == "L":
            if ticks==1:
                self.waypoint["x"] = -y
                self.waypoint["y"] = x
            if ticks==2:
                self.waypoint["x"] = -x
                self.waypoint["y"] = -y
            if ticks==3:
                self.waypoint["x"] = y
                self.waypoint["y"] = -x
        print("Turned waypoint" + instruction["command"] + "%d degrees (%d ticks)."%(instruction["val"],ticks))
        print("Waypoint now: " + str(self.waypoint))

    def action(self, instruction):
        print("Actioning: " + str(instruction))
        if instruction["command"]=="L" or instruction["command"]=="R":
            self.turn(instruction)
        elif  instruction["command"]=="F":
            self.forward(instruction)
        else:
            self.move(instruction)

    def getManhattanDistance(self):
        return abs(self.mDistance["x"]) + abs(self.mDistance["y"])

    def __init__(self, x, y):
        self.waypoint = {"x" : x, "y" : y}

def readInput():
    text_file = open("input.txt", "r")
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
    ferry = Ferry(10,1)
    print(ferry.mDistance)
    instructions = readInput()
    for instruction in instructions:
        ferry.action(instruction)
    print(ferry.getManhattanDistance())

if __name__ == "__main__":
    main()
