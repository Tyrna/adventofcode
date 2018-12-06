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
    return (len(line) -1)

f = open("input.txt", "r+")


xd = f.readline()
read = xd
result = []

for i in range(65, 91):
    read = read.replace(chr(i),'')
    read = read.replace(chr(i+32),'')
    while True:
        read = getStuff(read)
        if isinstance(read, int):
            break
    
    print("Done with ", chr(i) )
    result.append(read)
    read = xd
    notDone = False

print(min(result))
            