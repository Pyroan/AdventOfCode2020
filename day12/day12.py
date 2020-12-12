with open('day12.txt') as f:
    l = []
    for line in f:
        l.append((line[0], int(line[1:])))


pos = [0, 0]
bearing = 0


def move(d, dis):
    if d == 'N':
        pos[1] += dis
    elif d == 'S':
        pos[1] -= dis
    elif d == 'E':
        pos[0] += dis
    elif d == 'W':
        pos[0] -= dis


for i in l:
    if i[0] in "NSEW":
        move(i[0], i[1])
    elif i[0] == 'L':
        bearing += i[1]
        if bearing >= 360:
            bearing -= 360
    elif i[0] == 'R':
        bearing -= i[1]
        if bearing < 0:
            bearing += 360
    elif i[0] == 'F':
        move("ENWS"[bearing // 90], i[1])

print(sum(map(abs, pos)))
