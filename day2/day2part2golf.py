print(sum([(p[int(n[0])-1]==o)^(p[int(n[1])-1]==o)for n,o,p in[(j.split('-'),k[0],l)for j,k,l in[x.split()for x in open('day2.txt').readlines()]]]))