with open('day10.txt') as f:
    l = list(map(int, f.readlines()))

m = max(l)+3
l = sorted(l)
l = [0] + l + [m]

ways = 0
lookup = [0] * len(l)
lookup[-1] = 1
for i in reversed(range(len(l)-1)):
    for j in range(i, len(l)):
        if l[j]-l[i] > 3:
            break
        lookup[i] += lookup[j]

print(lookup[0])
