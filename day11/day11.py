from copy import deepcopy
from collections import Counter
with open('day11.txt') as f:
    l = list(map(list, map(str.strip, f.readlines())))

# who's ready for cellular automata
changed = True
while changed:
    changed = False
    prev = deepcopy(l)
    for i in range(len(l)):
        for j in range(len(l[i])):
            count = 0
            # adjacent crap
            if i > 0 and prev[i-1][j] == '#':
                count += 1
            if i > 0 and j > 0 and prev[i-1][j-1] == '#':
                count += 1
            if j > 0 and prev[i][j-1] == '#':
                count += 1
            if i < len(l)-1 and prev[i+1][j] == '#':
                count += 1
            if j < len(l[i])-1 and prev[i][j+1] == '#':
                count += 1
            if i < len(l)-1 and j < len(l[i])-1 and prev[i+1][j+1] == '#':
                count += 1
            if i > 0 and j < len(l[i])-1 and prev[i-1][j+1] == '#':
                count += 1
            if i < len(l) - 1 and j > 0 and prev[i+1][j-1] == '#':
                count += 1

            if prev[i][j] == 'L' and count == 0:
                l[i][j] = '#'
                changed = True
            elif prev[i][j] == '#' and count >= 4:
                l[i][j] = 'L'
                changed = True

print(sum(map(lambda x: Counter(x)['#'], l)))
