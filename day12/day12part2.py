with open('day12.txt') as f:
    l = []
    for line in f:
        l.append((line[0], int(line[1:])))


pos = [0, 0]
wp = [10, 1]


def move(d, dis):
    if d == 'N':
        wp[1] += dis
    elif d == 'S':
        wp[1] -= dis
    elif d == 'E':
        wp[0] += dis
    elif d == 'W':
        wp[0] -= dis


for i in l:
    if i[0] in "NSEW":
        move(i[0], i[1])
    # I think this is neat/elegant
    # ...even though it's just how the math works
    elif i[0] == 'L':
        for i in range(i[1]//90):
            wp.reverse()
            wp[0] = -wp[0]
    elif i[0] == 'R':
        for i in range(i[1]//90):
            wp.reverse()
            wp[1] = -wp[1]
    elif i[0] == 'F':
        pos[0] += wp[0] * i[1]
        pos[1] += wp[1] * i[1]

print(sum(map(abs, pos)))
