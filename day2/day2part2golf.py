# Just a small golf, as a snack.
print(sum((c[int(a.split('-')[0])-1]==o[0])^(c[int(a.split('-')[1])-1]==o[0])for a,o,c in map(str.split,open('day2.txt'))))