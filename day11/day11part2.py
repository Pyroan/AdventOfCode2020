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
            if prev[i][j] != '.':
                count = 0
                # adjacent crap
                # right
                k = j
                while k < len(l[i])-1:
                    k += 1
                    if prev[i][k] == 'L':
                        break
                    elif prev[i][k] == '#':
                        count += 1
                        break
                # left
                k = j
                while k > 0:
                    k -= 1
                    if prev[i][k] == 'L':
                        break
                    elif prev[i][k] == '#':
                        count += 1
                        break

                # up
                k = i
                while k > 0:
                    k -= 1
                    if prev[k][j] == 'L':
                        break
                    elif prev[k][j] == '#':
                        count += 1
                        break

                # down
                k = i
                while k < len(l)-1:
                    k += 1
                    if prev[k][j] == 'L':
                        break
                    elif prev[k][j] == '#':
                        count += 1
                        break

                # up-left
                k, m = i, j
                while k > 0 and m > 0:
                    k -= 1
                    m -= 1
                    if prev[k][m] == 'L':
                        break
                    elif prev[k][m] == '#':
                        count += 1
                        break

                # up-right
                k, m = i, j
                while k > 0 and m < len(l[i])-1:
                    k -= 1
                    m += 1
                    if prev[k][m] == 'L':
                        break
                    elif prev[k][m] == '#':
                        count += 1
                        break

                # down-left
                k, m = i, j
                while k < len(l)-1 and m > 0:
                    k += 1
                    m -= 1
                    if prev[k][m] == 'L':
                        break
                    elif prev[k][m] == '#':
                        count += 1
                        break

                # down-right
                k, m = i, j
                while k < len(l)-1 and m < len(l[i])-1:
                    k += 1
                    m += 1
                    if prev[k][m] == 'L':
                        break
                    elif prev[k][m] == '#':
                        count += 1
                        break
                # print(count, end='')
                if prev[i][j] == 'L' and count == 0:
                    l[i][j] = '#'
                    changed = True
                elif prev[i][j] == '#' and count >= 5:
                    l[i][j] = 'L'
                    changed = True
    #         else:
    #             print(' ', end='')
    #     print()
    # print('\n'.join(map(''.join, l)))
    # print()

print(sum(map(lambda x: Counter(x)['#'], l)))
