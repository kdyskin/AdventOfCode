import copy

class ConwayCubes:
    def __init__(self, file):
        text_file = open(file, "r")
        lines = text_file.readlines()
        self.pocketDimension = []
        x = []
        for line in lines:
            y = []
            for c in line.strip():
                y.append(c)
            x.append(y)
        self.pocketDimension.append(x)
        text_file.close()

    def print(self):
        for z in range(len(self.pocketDimension)):
            print("z=%d"%z)
            for y in range(len(self.pocketDimension[z])):
                for x in range(len(self.pocketDimension[z][y])):
                    print(self.pocketDimension[z][y][x], end="")
                print("")
        print("%dx%dx%d"%(len(self.pocketDimension),len(self.pocketDimension[0]),len(self.pocketDimension[0][0])))
        #input("Press Enter to continue...")

    def printCopy(self,c):
        for z in range(len(c)):
            print("z=%d"%z)
            for y in range(len(c[z])):
                for x in range(len(c[z][y])):
                    print(c[z][y][x], end="")
                print("")
            print("")

    def strip(self):
        #check if front (z=0) and back (z=length-1) are inactive and if so delete
        keepChecking = True
        while keepChecking:
            keepChecking = False
            for z in [len(self.pocketDimension)-1, 0]:
                pop = True
                for y in range(len(self.pocketDimension[z])):
                    for x in range(len(self.pocketDimension[z][y])):
                        if self.pocketDimension[z][y][x]=="#":
                            pop = False
                            break
                    if not pop:
                        break
                if pop:
                    keepChecking = True
                    self.pocketDimension.pop(z)

            #check if top (y=0) and bottom (y=length-1) are inactive and if so delete
            for z in range(len(self.pocketDimension)):
                pop = True
                y = len(self.pocketDimension[z])-1
                for x in range(len(self.pocketDimension[z][y])):
                    if self.pocketDimension[z][y][x]=="#":
                        pop = False
                        #print("(%d,%d,%d) is active, cannot remove bottom layer"%(z,y,x))
                        #print(self.pocketDimension[z][y])
                        break
                if not pop:
                    break
                if pop:
                    keepChecking = True
                    self.pocketDimension[z].pop(y)
            #check if top (y=0) and bottom (y=length-1) are inactive and if so delete
            for z in range(len(self.pocketDimension)):
                pop = True
                y = 0
                for x in range(len(self.pocketDimension[z][y])):
                    if self.pocketDimension[z][y][x]=="#":
                        pop = False
                        #print("(%d,%d,%d) is active, cannot remove top layer"%(z,y,x))
                        #print(self.pocketDimension[z][y])
                        break
                if not pop:
                    break
                if pop:
                    keepChecking = True
                    self.pocketDimension[z].pop(y)

            #check if left (x=0) and right (x=length-1) are inactive and if so delete
            for z in range(len(self.pocketDimension)):
                pop = True
                for y in range(len(self.pocketDimension[z])):
                    x = len(self.pocketDimension[z][y])-1
                    if self.pocketDimension[z][y][x]=="#":
                        pop = False
                        break
                if not pop:
                    break
                if pop:
                    keepChecking = True
                    for y in range(len(self.pocketDimension[z])):
                        self.pocketDimension[z][y].pop(x)
            #check if left (x=0) and right (x=length-1) are inactive and if so delete
            for z in range(len(self.pocketDimension)):
                pop = True
                for y in range(len(self.pocketDimension[z])):
                    x = 0
                    if self.pocketDimension[z][y][x]=="#":
                        pop = False
                        break
                if not pop:
                    break
                if pop:
                    keepChecking = True
                    for y in range(len(self.pocketDimension[z])):
                        self.pocketDimension[z][y].pop(x)

    def pad(self):
        for z in range(len(self.pocketDimension)):
            for y in range(len(self.pocketDimension[z])):
                self.pocketDimension[z][y].insert(0, ".")
                self.pocketDimension[z][y].append(".")
            self.pocketDimension[z].insert(0, ["." for i in range(len(self.pocketDimension[z][y]))])
            self.pocketDimension[z].append(["." for i in range(len(self.pocketDimension[z][y]))])
        self.pocketDimension.insert(0, [["." for i in range(len(self.pocketDimension[0]))] for j in range(len(self.pocketDimension[0][0]))])
        self.pocketDimension.append(   [["." for i in range(len(self.pocketDimension[0]))] for j in range(len(self.pocketDimension[0][0]))])

    def countActiveNeighbors(self,z,y,x):
        count = 0
        #c = 0
        zs = [z]
        ys = [y]
        xs = [x]
        if z-1>=0: zs.append(z-1)
        if z+1<len(self.pocketDimension): zs.append(z+1)
        if y-1>=0: ys.append(y-1)
        if y+1<len(self.pocketDimension[0]): ys.append(y+1)
        if x-1>=0: xs.append(x-1)
        if x+1<len(self.pocketDimension[0][0]): xs.append(x+1)
        for zz in zs:
            for yy in ys:
                for xx in xs:
                    if xx == x and yy == y and zz == z:
                        continue
                    if self.pocketDimension[zz][yy][xx] == "#":
                        count += 1
        #            c += 1
        #print("For (%d,%d,%d) %d neighbors were checked.Coordinates arrays are:"%(z,y,x,c))
        #print(zs)
        #print(ys)
        #print(xs)
        return count

    def countActive(self):
        count = 0
        for z in range(len(self.pocketDimension)):
            for y in range(len(self.pocketDimension[z])):
                for x in range(len(self.pocketDimension[z][y])):
                    if self.pocketDimension[z][y][x] == "#":
                        count += 1
        return count

    def cycle(self):
        self.pad()
        c = copy.deepcopy(self.pocketDimension)
        for z in range(len(self.pocketDimension)):
            for y in range(len(self.pocketDimension[z])):
                for x in range(len(self.pocketDimension[z][y])):
                    count = self.countActiveNeighbors(z,y,x)
                    #c[z][y][x] = "*"
                    #self.printCopy(c)
                    isActive = (self.pocketDimension[z][y][x] == "#")
                    state = "inactive"
                    if isActive:
                         state = "active"
                    #print("(%d,%d,%d) is %s and has %d active neighbours"%(z,y,x,state,count))
                    if self.pocketDimension[z][y][x] == "#":
                        if count in [2,3]:
                            c[z][y][x] = "#"
                        else:
                            c[z][y][x] = "."
                    else:
                        if count == 3:
                            c[z][y][x] = "#"
                        else:
                            c[z][y][x] = "."

        self.pocketDimension = c
        #self.strip()
        self.print()

def main():
    cubes = ConwayCubes("input.txt")

    for _ in range(6):
        cubes.cycle()

    print(cubes.countActive())

if __name__ == "__main__":
    main()
