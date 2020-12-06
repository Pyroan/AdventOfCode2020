with open('day6.txt') as f:
    l = map(str.split, f.read().split('\n\n'))

count = 0
for group in l:
    qs = []
    for p in group:
        qs += list(p)
    qs = set(qs)
    print(len(qs))
    count += len(qs)

print(count)
