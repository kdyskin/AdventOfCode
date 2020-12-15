def readInput():
    text_file = open("input.txt", "r")
    lines = text_file.readlines()
    input = []
    for line in lines:
        input.append(int(line.strip()))
    text_file.close()
    return input

def buildPreamble(size,list):
    preamble = []
    for i in range(0,size):
        preamble.append(list.pop(0))
    return preamble

def isValidNumber(n,preamble):
    for i in range(0,len(preamble)):
        for j in range(i+1,len(preamble)):
            if preamble[i]+preamble[j] == n:
                return True
    return False

def findNumber(preamble,list):
    size = len(preamble)
    while len(list)>0:
        if isValidNumber(list[0],preamble):
            preamble.pop(0)
            preamble.append(list.pop(0))
        else:
            print("%d Is invalid for "%list[0])
            print(preamble)
            break

def findContiguousSet(arr, sum):
    n = len(arr)
    subset = []
    # Pick a starting
    # point
    for i in range(n):
        curr_sum = arr[i]
        # try all subarrays
        # starting with 'i'
        j = i + 1
        while j <= n:
            if curr_sum == sum:
                print ("Sum found between")
                print("indexes % d and % d"%( i, j-1))
                for inx in range(i,j):
                    subset.append(arr[inx])
                return subset
            if curr_sum > sum or j == n:
                break
            curr_sum = curr_sum + arr[j]
            j += 1
    print ("No subarray found")
    return subset

def main():
    input = readInput()
    preambleSize = 25
    preamble = buildPreamble(preambleSize,input)
    #print(preamble,input)
    findNumber(preamble,input)
    #Part 2
    contiguesSet = findContiguousSet(readInput(),input[0])
    contiguesSet.sort()
    #here is the sum of min and max in the subset
    print("Sum of min and max is %d"%(contiguesSet[0]+contiguesSet[-1]))

if __name__ == "__main__":
    main()
