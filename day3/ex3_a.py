# in_file = 'd3_test_in.txt'
in_file = 'd3_a_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

sum_1 = [0] * len(data[0])

for line in data:
    for idx, char in enumerate(line):
        sum_1[idx] += int(char)

# print(len(data))
# print(sum_1)
gamma = []
epsilon = []
for i in sum_1:
    if i > (len(data)-i):
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

print(gamma)
print(epsilon)
