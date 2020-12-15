#def

def main():
    input = [2,15,0,9,1,20]
    #input = [0,3,6]
    #input = [1,3,2]
    #input = [2,1,3]
    numbers = {}
    turns = []
    for i in range(30000000):
        if i<len(input):
            numbers[input[i]] = [i+1]
            turns.append(input[i])
        else:
            if len(numbers[turns[-1]])==1:
                #first time spoken
                turns.append(0)
                #if len(numbers[0])>1:
                #    numbers[0].pop(0)
                if 0 in numbers:
                    numbers[0].append(i+1)
                else:
                    numbers[0] = [i+1]
            else:
                #print(numbers[turns[-1]])
                n = numbers[turns[-1]][-1]-numbers[turns[-1]][-2]
                turns.append(n)
                if n in numbers:
                    numbers[n].append(i+1)
                else:
                    numbers[n] = [i+1]


    print(turns[-1])
    #print(numbers)
if __name__ == "__main__":
    main()
