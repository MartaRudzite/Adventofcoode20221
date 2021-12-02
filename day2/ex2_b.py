# in_file = 'd2_test_in.txt'
in_file = 'd2_a_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

data = [i.split() for i in data]
xy = 0
z = 0
aim = 0
for line in data:
    if line[0] == 'forward':
        xy += int(line[1])
        z += aim * int(line[1])
    elif line[0] == 'down':
        aim += int(line[1])
    elif line[0] == 'up':
        aim -= int(line[1])
    else:
        print('This is not working as expected')

print(xy*z)
