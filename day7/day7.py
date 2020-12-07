# Reverse dictionary time
with open('day7.txt') as f:
    rules = {}
    for line in f:
        l = line.split('contain')  # i know
        parent = '_'.join(l[0].split()[:2])
        if 'no other bags.' not in l[1]:
            children = l[1].split(', ')
            for child in children:
                c = '_'.join(child.split()[1:3])
                if c not in rules:
                    rules[c] = []
                rules[c].append(parent)
# Ugh this is gonna have internal loops i can feel it


def traverse(root):
    if root not in rules:
        return []
    l = rules[root][:]
    for r in rules[root]:
        l = l + traverse(r)
    return l


print(len(set(traverse('shiny_gold'))))
