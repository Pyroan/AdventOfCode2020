from copy import deepcopy

# Hi, I'm Bruce.
# Bruce Force.
with open('day8.txt') as f:
    instructions = [x.split() for x in f.readlines()]

for i in range(len(instructions)):
    l = deepcopy(instructions)

    if l[i][0] == 'jmp':
        l[i][0] = 'nop'
    elif l[i][0] == 'nop':
        l[i][0] = 'jmp'

    ip = 0
    visited = [False] * len(l)
    acc = 0
    while ip < len(l):
        if visited[ip]:
            break
        visited[ip] = True
        if l[ip][0] == 'acc':
            acc += int(l[ip][1])
        elif l[ip][0] == 'jmp':
            ip += int(l[ip][1])
            continue
        elif l[ip][0] == 'nop':
            pass
        ip += 1
    if ip == len(l):
        print(acc)
        exit()
