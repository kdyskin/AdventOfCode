def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    input = []
    for line in lines:
        input.append(line.strip())
    return input

def e(stack):
    tillOpenBracket = False
    if stack[-1] == ")":
        tillOpenBracket = True
        stack.pop()
    while len(stack)>=3:
        if stack[-2]=="(" and not tillOpenBracket:
            break
        v1 = stack.pop()
        op = stack.pop()
        v2 = stack.pop()
        if op == "+":
            stack.append(v1+v2)
        else:
            stack.append(v1*v2)
        if tillOpenBracket and stack[-2]=="(":
            val = stack.pop()
            stack.pop()
            stack.append(val)
            break

def evaluate(exp):
    stack = []
    pStack = []
    plusIn = False
    for c in exp:
        if c==" ":
            continue
        if c in ["+","*"]:
            if plusIn and c == "*":
                e(stack)
                plusIn = False

            if c == "+":
                plusIn = True
            stack.append(c)
        else:
            if c in ["(",")"]:
                stack.append(c)
                if c == "(":
                    pStack.append(plusIn)
                    plusIn = False

                if c == ")":
                    #import pdb; pdb.set_trace()
                    e(stack)
                    if len(pStack)>0:
                        plusIn = pStack.pop()
            else:
                stack.append(int(c))
    e(stack)
    print("%s = %d [IN VOODOO MATH]"%(exp,stack[0]))
    return stack[0]

def main():
    expressions = readInput()
    sum = 0
    for exp in expressions:
        sum += evaluate(exp)
    print(sum)

if __name__ == "__main__":
    main()
