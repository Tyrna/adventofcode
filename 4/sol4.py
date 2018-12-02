f = open("input.txt", "r+")
myList = []

for line in f.readlines():
    #For each string we've seen...
    for strings in myList:
        miss = 0
        #Check character differences...
        for i in range(len(strings)):
            if (line[i] != strings[i]):
                miss = miss + 1
                pos = i
                #Move on if more than 1...
                if (miss == 2):
                    break

        #If less than two differences, print line without given difference...
        if (miss != 2):
            line = line[:pos] + line[(pos+1):]
            print("Solution: " , line)
            exit(0)

    myList.append(list(line[:-1]))