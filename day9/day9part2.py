with open('day9.txt') as f:
    l = list(map(int, f.readlines()))

key = 0
for i in range(25, len(l)):
    pre = l[i-25:i]
    valid = False
    for j in pre[::-1]:
        if l[i] - j in pre:
            valid = True
    if not valid:
        key = l[i]
        break

start = 0
while start < len(l):
    total = l[start]
    end = start+1
    while total < key and end < len(l):
        total += l[end]
        end += 1
    if total == key:
        print(key)
        print(min(l[start:end]) + max(l[start:end]))
        exit()
    start += 1
