with open('day3.txt') as f:
    l = list(map(str.strip, f.readlines()))

count = 0
j = 0
for i in range(len(l)):
    if l[i][j] == '#':
        count += 1
    j += 3
    if j >= len(l[0]):
        j -= len(l[0])
print(count)
