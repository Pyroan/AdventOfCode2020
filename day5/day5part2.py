with open('day5.txt') as f:
    l = f.readlines()

seats = [False]*128*8
for line in l:
    line = line.replace('F', '0')
    line = line.replace('B', '1')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    row = int(line[:-4], 2)
    col = int(line[-4:], 2)

    seats[row*8+col] = True

for i in range(1, len(seats)-1):
    if seats[i] == False and seats[i-1] == True and seats[i+1] == True:
        print(i)
