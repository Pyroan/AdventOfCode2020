# Just a small golf, as a snack.
print(sum([(n[2][int(n[0][0])-1]==n[1])^(n[2][int(n[0][1])-1]==n[1])for n in[[m[0].split('-'),m[1][0],m[2]]for m in[x.split()for x in open('day2.txt').readlines()]]]))
