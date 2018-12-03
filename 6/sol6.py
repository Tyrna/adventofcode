f = open("input.txt", "r+")

map = [[0 for x in range(1000)] for y in range(1000)]

lines = f.readlines()

for line in lines:
    line = line.split(" ")
    pos = line[2].split(",")
    pos[1] = pos[1][:-1]
    area = line[3].split("x")
    area[1] = area[1][:-1]

    for wide in range(0, int(area[0])):
        y = int(pos[0]) + wide
        for tall in range(0, int(area[1])):
            x = int(pos[1]) + tall
            map[x][y] = map[x][y] + 1

#xD
for line in lines:
    line = line.split(" ")
    pos = line[2].split(",")
    pos[1] = pos[1][:-1]
    area = line[3].split("x")
    area[1] = area[1][:-1]

    found = False
    for wide in range(0, int(area[0])):
        y = int(pos[0]) + wide
        for tall in range(0, int(area[1])):
            x = int(pos[1]) + tall
            if (map[x][y] > 1):
                found = True
                break
        if (found):
            break
    if (not found):
        print(line[0])
