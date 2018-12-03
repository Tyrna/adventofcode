f = open("input.txt", "r+")

map = [[0 for x in range(1000)] for y in range(1000)]

for line in f.readlines():
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

num = 0
for x in map:
    for y in x:
        if (y > 1):
            num = num + 1

print(num)