with open('day5.txt') as f:
    l = f.readlines()

biggest = -1
for line in l:
    line = line.replace('F', '0')
    line = line.replace('B', '1')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    row = int(line[:-4], 2)
    col = int(line[-4:], 2)
    x = row*8 + col
    if x > biggest:
        biggest = x

print(biggest)
