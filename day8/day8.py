with open('day8.txt') as f:
    l = [x.split() for x in f.readlines()]

ip = 0
visited = [False] * len(l)
acc = 0
while ip < len(l):
    if visited[ip]:
        print(acc)
        exit()
    visited[ip] = True
    if l[ip][0] == 'acc':
        acc += int(l[ip][1])
    elif l[ip][0] == 'jmp':
        ip += int(l[ip][1])
        continue
    elif l[ip][0] == 'nop':
        pass
    ip += 1
