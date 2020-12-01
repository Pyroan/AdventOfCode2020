with open('day1.txt') as f:
    l = list(map(int, f.readlines()))

for i in range(len(l)):
    for j in range(len(l[i:])):
        if l[i]+l[j] == 2020:
            print(l[i]*l[j])
            exit()
