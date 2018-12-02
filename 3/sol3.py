f = open("input.txt", "r+")

i = 0
two = False
twoNum = 0
three = False
threeNum = 0
map = {}

for line in f.readlines():
    #Fill the map
    for char in line:
        if char in map:
            map[char] = map[char] + 1
        else:
            map[char] = 1

    #Check the map
    for char in map:
        if map[char] == 2:
            two = True
        if map[char] == 3:
            three = True

    #Save the info
    if (two):
        twoNum = twoNum + 1
    if (three):
        threeNum = threeNum + 1

    map = {}
    two = False
    three = False

print("Checksum: " , twoNum * threeNum)