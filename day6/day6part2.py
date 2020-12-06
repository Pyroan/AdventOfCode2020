from collections import Counter
with open('day6.txt') as f:
    l = map(str.split, f.read().split('\n\n'))

count = 0
for group in l:
    qs = []
    for p in group:
        qs += list(p)
    qs = Counter(qs)

    c = len(list(filter(lambda x: qs[x] == len(group), qs)))
    count += c

print(count)
