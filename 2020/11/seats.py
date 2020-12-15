def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    #start with 0 -> charging outlet
    input = []
    for line in lines:
        row = []
        for c in line.strip():
            row.append(c)
        input.append(row)
    text_file.close()
    return input

def changeSeat(seatLayout,r,c):
    n = 0
    rows = len(seatLayout)
    cols = len(seatLayout[0])
    if (r-1)>=0 and (c-1)>=0:
        if seatLayout[r-1][c-1] == "#":
            n += 1
    if (r-1)>=0:
        if seatLayout[r-1][c] == "#":
            n += 1
    if (r-1)>=0 and (c+1)<cols:
        if seatLayout[r-1][c+1] == "#":
            n += 1
    if (c-1)>=0:
        if seatLayout[r][c-1] == "#":
            n += 1
    if (c+1)<cols:
        if seatLayout[r][c+1] == "#":
            n += 1
    if (r+1)<rows and (c-1)>=0:
        if seatLayout[r+1][c-1] == "#":
            n += 1
    if (r+1)<rows:
        if seatLayout[r+1][c] == "#":
            n += 1
    if (r+1)<rows and (c+1)<cols:
        if seatLayout[r+1][c+1] == "#":
            n += 1

    if seatLayout[r][c]=="#" and n>=4:
        return True
    if seatLayout[r][c]=="L" and n==0:
        return True
    return False

def shuffle(seatLayout):
    rows = len(seatLayout)
    cols = len(seatLayout[0])
    shuffledSeatLayout = []
    for row in seatLayout:
        shuffledSeatLayout.append(row.copy())

    for r in range(rows):
        for c in range(cols):
            if seatLayout[r][c] == ".":
                continue
            if changeSeat(seatLayout,r,c):
                if seatLayout[r][c] == "L":
                    shuffledSeatLayout[r][c] = "#"
                else:
                    shuffledSeatLayout[r][c] = "L"
    drawMap(seatLayout)
    print("Changes to:")
    drawMap(shuffledSeatLayout)
    return shuffledSeatLayout

def drawMap(seatLayout):
    for row in seatLayout:
        r = ""
        for seat in row:
            r += seat
        print(r)

def compareLayouts(l1,l2):
    rows = len(l1)
    cols = len(l1[0])
    for r in range(rows):
        for c in range(cols):
            if l1[r][c] != l2[r][c]:
                return True
    return False

def countOccupied(seatLayout):
    rows = len(seatLayout)
    cols = len(seatLayout[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if seatLayout[r][c] == "#":
                count += 1
    return count

def main():
    seatLayout = readInput()
    changed = True
    while changed:
        newLayout = shuffle(seatLayout)
        changed = compareLayouts(seatLayout,newLayout)
        if changed:
            seatLayout = newLayout
    print(countOccupied(seatLayout))

if __name__ == "__main__":
    main()
