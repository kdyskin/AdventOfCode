def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    input = []
    for line in lines:
        input.append(line.strip())
    return input

def evaluate(exp):
    vals = []
    ops = []
    for c in exp:
        if c==" ":
            continue
        if c in ["+","*"]:
            ops.append(c)
        else:
            if c in ["(",")"]:
                vals.append(c)
            else:
                vals.append(int(c))
    iOps = 0
    iVals = 0
    while len(vals)>1:
        if type(vals[iVals]) == int:
            if type(vals[iVals+1]) == int:
                op = ops.pop(iOps)
                v1 = int(vals.pop(iVals))
                v2 = int(vals.pop(iVals))
                if op == "*":
                    vals.insert(iVals,v1*v2)
                else:
                    vals.insert(iVals,v1+v2)
                if iVals > 0 and type(vals[iVals]) == int and vals[iVals-1] == "(" and vals[iVals+1] == ")":
                    iVals -= 1
                    vals.pop(iVals)
                    vals.pop(iVals+1)

            else:
                if vals[iVals] == "(":
                    vals.pop(iVals)
                    iOps += 1
                    iVals += 1
                if vals[iVals] == ")":
                    vals.pop(iVals)
                    iOps -= 1
                    iVals -= 1
                if vals[iVals+1] == "(":
                    vals.pop(iVals+1)
                    iOps += 1
                    iVals += 1
                if vals[iVals+1] == ")":
                    vals.pop(iVals+1)
                    iOps -= 1
                    iVals -= 1
        elif vals[iVals] == "(":
            iVals += 1

    print("%s = %d [IN VOODOO MATH]"%(exp,vals[0]))
    return vals[0]

def main():
    expressions = readInput()
    sum = 0
    for exp in expressions:
        sum += evaluate(exp)
    print(sum)

if __name__ == "__main__":
    main()
