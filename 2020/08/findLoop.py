def readInstructions():
    instructions = []
    text_file = open("input.txt", "r")
    input = text_file.readlines()
    for line in input:
        dict = {}
        l = line.strip().split()
        dict["com"] = l[0]
        dict["param"] = int(l[1])
        dict["ran"] = False
        instructions.append(dict)
    return instructions

def runProgram(inst):
    accumulator = 0
    i = 0
    while i < len(inst):
        if inst[i]["ran"]:
            print(accumulator)
            return False
        elif inst[i]["com"] == "acc":
            #print("Executing " + str(inst[i]))
            accumulator += inst[i]["param"]
            #print(accumulator)
            inst[i]["ran"] = True
            i += 1
        elif inst[i]["com"] == "jmp":
            #print("Executing " + str(inst[i]))
            inst[i]["ran"] = True
            i += inst[i]["param"]
            #print(i)
        else:
            #print("Executing " + str(inst[i]))
            inst[i]["ran"] = True
            i += 1
            #print(i)
    print(accumulator)
    return True

def resetInstructions(instructions):
    for instruction in instructions:
        instruction["ran"] = False
        #print(instruction)
    return instructions

def getNextInstructionsCandidate(fromIndex,instructions):
    dict = {}
    for i in range(fromIndex,len(instructions)):
        if instructions[i]["com"] == "jmp":
            dict["index"] = i
            instructions[i]["com"] = "nop"
            dict["instructions"] = resetInstructions(instructions)
            break
        if instructions[i]["com"] == "nop":
            dict["index"] = i
            instructions[i]["com"] = "jmp"
            dict["instructions"] = resetInstructions(instructions)
            break
    return dict

def main():
    i = 0
    inst = readInstructions()
    #Part 1
    runProgram(inst)

    #Part 2
    while i<len(inst):
        d = getNextInstructionsCandidate(i,readInstructions())
        if runProgram(d["instructions"]):
            break
        else:
            i = d["index"] + 1
            print("Moving on to :" + str(i))

if __name__ == "__main__":
    main()
