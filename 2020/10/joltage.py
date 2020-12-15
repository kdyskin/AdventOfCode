def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    #start with 0 -> charging outlet
    input = [0]
    for line in lines:
        input.append(int(line.strip()))
    text_file.close()
    input.sort()
    #devices built-in adaptor is 3 jolts higher
    input.append(input[-1]+3)
    return input

def createKey(list):
    s = ""
    for n in list:
        s += str(n)+"."
    return s

def countArrangements(index,input,d):
    optionsFromHere = 1
    key = createKey(input)
    if key not in d:
        d[key] = input
    #print(index)
    if index>2:
        #print(input," --> this is whithout having to remove %d"%input[index-1])
        optionsFromHere += countArrangements(index-1,input,d)
        if input[index]-input[index-2]<4:
            #we can pop middle number and still have valid chain
            list = input.copy()
            #print("%d can be removed"%list[index-1])
            list.pop(index-1)
            #print(list, " ==> this is whith %d removed"%input[index-1])
            optionsFromHere += countArrangements(index-1,list,d)


    return optionsFromHere

def main():
    input = readInput()
    print(input)
    step1 = 0
    step3 = 0
    for i in range(1,len(input)):
        if (input[i]-input[i-1]) == 1:
            step1 += 1
        if (input[i]-input[i-1]) == 3:
            step3 += 1
        print("From %d to %d 1-jolt=%d and 3-jolt=%d"%(input[i-1],input[i],step1,step3))

    print("Answer to 1 is %d"%(step1*step3))

    #part2
    dict = {}
    print("Answer to 2 is %d"%countArrangements(len(input)-1,input,dict))
    print(len(dict))

if __name__ == "__main__":
    main()
