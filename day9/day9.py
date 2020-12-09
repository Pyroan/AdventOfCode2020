with open('day9.txt') as f:
    l = list(map(int, f.readlines()))

for i in range(25, len(l)):
    pre = l[i-25:i]
    valid = False
    for j in pre[::-1]:
        if l[i] - j in pre:
            valid = True
    if not valid:
        print(l[i])
        exit()
