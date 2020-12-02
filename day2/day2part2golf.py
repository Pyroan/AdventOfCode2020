# Just a small golf, as a snack.
print(sum([(n['p'][int(n['c'][0])-1]==n['t'])^(n['p'][int(n['c'][1])-1]==n['t'])for n in[{'c':m[0].split('-'),'t':m[1][0],'p':m[2]}for m in[x.split()for x in open('day2.txt').readlines()]]]))
