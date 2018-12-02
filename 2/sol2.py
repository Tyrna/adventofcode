f = open("input.txt", "r+")
sol = 0
map = {}
done = False
lines = f.readlines()

while (True):
    for line in lines:
        sol = sol + int(line)
        if sol in map:
            print(sol)
            done = True
            break
        map[sol] = 1
    if (done):
        break