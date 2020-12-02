from collections import Counter
l = []
with open('day2.txt') as f:
    for line in f.readlines():
        node = {}
        line = line.strip().split(' ')
        node['policy'] = list(map(int, line[0].split('-')))
        node['target'] = line[1][0]
        node['pw'] = line[2]

        l.append(node)

count = 0
for node in l:
    c = Counter(node['pw'])[node['target']]
    if node['policy'][0] <= c <= node['policy'][1]:
        count += 1
        print(node)

print(count)
