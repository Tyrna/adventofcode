f = open("input.txt", "r+")
sol = 0

for line in f.readlines():
    sol = sol + int(line)

print(sol)