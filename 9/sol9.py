def getStuff(line):
    for i in range(0, len(line)-1):
        #upper
        if ord(line[i]) < 97 :
            if ord(line[i+1]) - ord(line[i]) - 32 == 0:
                line = line[:i] + line[i+2:]
                return line
        else:
            if ord(line[i+1]) - ord(line[i]) + 32 == 0:
                line = line[:i] + line[i+2:]
                return line
    
    print(len(line)-1)
    exit(0)

f = open("input.txt", "r+")


read = f.readline()
result = []
while True:
    read = getStuff(read)

            