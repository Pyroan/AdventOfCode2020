# like yeah you can collapse this into a oneliner but it would suck because I can't think of a way to not repeat s (filter saves you one but still).
s=set(range(1024))-{int(l.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)for l in open('day5.txt')}
print([i for i in s if i-1 not in s and i+1 not in s])