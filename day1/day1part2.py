with open('day1.txt') as f:
    l = list(map(int, f.readlines()))

# It's day 1 who needs efficiency
# This better not be like the intcode thing where
# it comes back to ruin my life
for i in range(len(l)):
    for j in range(len(l[i:])):
        for k in range(len(l[j:])):
            if l[i]+l[j]+l[k] == 2020:
                print(l[i]*l[j]*l[k])
                exit()
