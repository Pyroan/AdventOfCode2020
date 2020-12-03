with open('day3.txt') as f:
    l = list(map(str.strip, f.readlines()))

speeds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = 1
for s in speeds:
    count = 0
    i = 0
    j = 0
    while i < len(l):
        if l[i][j] == '#':
            count += 1
        j += s[0]
        if j >= len(l[0]):
            j -= len(l[0])
        i += s[1]
    trees *= count

print(trees)
