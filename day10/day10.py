with open('day10.txt') as f:
    l = list(map(int, f.readlines()))

l = sorted(l)
ones = 0
threes = 0
l = [0] + l + [max(l)+3]
for i in range(1, len(l)):
    if l[i] - l[i-1] == 1:
        ones += 1
    elif l[i] - l[i-1] == 3:
        threes += 1

print(ones*threes)
