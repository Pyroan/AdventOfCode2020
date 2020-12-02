# Just a small golf, as a snack.
print(sum([(p[int(n[0])-1]==o)^(p[int(n[1])-1]==o)for n,o,p in[(m[0].split('-'),m[1][0],m[2])for m in[x.split()for x in open('day2.txt').readlines()]]]))
