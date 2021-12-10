import copy

in_file = 'd7_test_in.txt'
# in_file = 'd7_in.txt'
data = [line.rstrip('\n').split(',') for line in open(in_file)]
# print(data)
data = [int(i) for i in data[0]]

min_sum = 1000000000
for i in range(min(data),max(data)):
    sum = 0
    for pos in data:
        dist = abs(i-pos)
        sum += (dist*(dist+1))/2
    if sum < min_sum:
        # print(i,sum,min_sum)
        min_sum = copy.deepcopy(sum)
        # print(min_sum)

print(int(min_sum))
