import datetime

f = open("input.txt", "r+")

lines = []
# Parse and sort info...
for line in f.readlines():
    line = line.split(" ")
    line[0] = line[0][1:]
    line[1] = line[1][:-1]
    lines.append(line)

lines = sorted(lines, key=lambda x: datetime.datetime.strptime(x[1], "%H:%M"))
lines = sorted(lines, key=lambda x: datetime.datetime.strptime(x[0], "%Y-%m-%d"))

#Welp
shifts = {}
onShift = -1
sleep = -1
wakes = -1

#Get the times they slept
for line in lines:
    if (line[2] == "Guard"):
        onShift = int(line[3][1:])
        sleep = -1
        wakes = -1
        continue
    if (line[2] == "falls"):
        sleep = (int(line[1][1:2]) *60) + (int(line[1][3:5]))
    if (line[2] == "wakes"):
        wakes = (int(line[1][1:2]) *60) + (int(line[1][3:5]))
        if onShift in shifts:
            shifts[onShift][0] = shifts[onShift][0] + (wakes-sleep)
            shifts[onShift].append((sleep, wakes))
        else:
            shifts[onShift] = []
            shifts[onShift].append(wakes-sleep)
            shifts[onShift].append((sleep, wakes))

#Find the sleepies dude
max = -1
who = -1
for person in shifts:
    if shifts[person][0] > max:
        max = shifts[person][0]
        who = person

map = {}
#Find which minute he slept the most
for hours in shifts[who][1:]:
    for i in range(hours[0], hours[1]):
        if i in map:
            map[i] = map[i] + 1
        else:
            map[i] = 1

max = -1
when = -1
#Find the most slept minut
for time in map:
    if map[time] > max:
        max = map[time]
        when = time

print(who * when)