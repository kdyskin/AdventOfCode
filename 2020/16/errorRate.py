class Tickets:
    def scanningErrorRate(self):
        errorRate = 0
        for ticket in self.nearbyTickets:
            for n in ticket:
                if not self.isValid(n):
                    errorRate += n
        return errorRate

    def isValid(self,n):
        for range in self.ranges:
            for value in range.values():
                if (value[0] <= n <= value[1]) or (value[2] <= n <= value[3]):
                    return True
        return False

    def deleteInvalid(self):
        i = 0
        while i<len(self.nearbyTickets):
            for n in self.nearbyTickets[i]:
                if not self.isValid(n):
                    self.nearbyTickets.pop(i)
                    i -= 1
                    continue
            i += 1

    def getMap(self):
        map = []
        for i in range(len(self.myTicket)):
            map.append([i,self.findPosition(i)])
        #while self.haveWorkToDo(self,map):
        map.sort(key = lambda x:len(x[1]))
        for i in range(len(map)):
            n = map[i][1][0]
            for j in range(i+1,len(map)):
                map[j][1].remove(n)
        map.sort(key = lambda x:x[1])
        return map

    def findPosition(self,index):
        self.deleteInvalid()
        candidates = []
        validTickets = self.nearbyTickets.copy()
        validTickets.append(self.myTicket)
        #print(validTickets)
        for i in range(len(self.ranges)): # <-- for each range
            allGood = True
            value = self.getValues(self.ranges[i])
            #print(value)
            for ticket in validTickets: # <-- check all valid tickets, number at "index" position is valid for ranges in "value"
                if (value[0] <= ticket[index] <= value[1]) or (value[2] <= ticket[index] <= value[3]):
                    continue
                allGood = False
            if allGood:
                candidates.append(i)
        return candidates

    def getValues(self,range):
        for value in range.values():
            return value

    def __init__(self, r, t, nbt):
        self.ranges = r
        self.myTicket = t
        self.nearbyTickets = nbt

def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    ranges = []
    nearbyTickets = []
    i = 0
    for l in range(i,len(lines)):
        line = lines[l].strip()
        i += 1
        if line == "":
            break
        ranges.append(createRange(line))
    i += 1
    ticket = [int(x) for x in lines[i].strip().split(",")]
    i += 3
    for l in range(i,len(lines)):
        nearbyTickets.append([int(x) for x in lines[l].strip().split(",")])
    text_file.close()
    tickets = Tickets(ranges,ticket,nearbyTickets)
    return tickets

def createRange(input):
    range = dict()
    kv = input.split(": ")
    vals = kv[1].split(" or ")
    lower = vals[0].split("-")
    upper = vals[1].split("-")
    range[kv[0]] = [int(lower[0]),int(lower[1]),int(upper[0]),int(upper[1])]
    return range

def main():
    tickets = readInput()
    #print(tickets.ranges)
    #print(tickets.myTicket)
    #print(tickets.nearbyTickets)
    print("Answer to 1 is %d"%tickets.scanningErrorRate())

    map = tickets.getMap()
    r2 = 1
    for m in map:
        if m[1][0]<6:
            r2 *= tickets.myTicket[m[0]]
    print("Answer to 2 is %d"%r2)

if __name__ == "__main__":
    main()
