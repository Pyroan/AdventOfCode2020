# Forward dictionary time
with open('day7.txt') as f:
    rules = {}
    for line in f:
        l = line.split('contain')  # i know
        parent = '_'.join(l[0].split()[:2])
        if parent not in rules:
            rules[parent] = []
        if 'no other bags.' not in l[1]:
            children = l[1].split(', ')
            for child in children:
                c = '_'.join(child.split()[1:3])
                if c not in rules:
                    rules[c] = []
                for _ in range(int(child.split()[0])):
                    rules[parent].append(c)


def traverse(root):
    if root not in rules:
        return []
    l = rules[root][:]
    for r in rules[root]:
        l = l + traverse(r)
    return l


print(len(traverse('shiny_gold')))
