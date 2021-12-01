# in_file = 'd1_test_in.txt'
in_file = 'd1_a_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

data = [int(i) for i in data]
rolling_sum = []
for i in range(2,len(data)):
    rolling_sum.append(data[i] + data[i-1] + data [i-2])

n_increase = 0
for i in range(1,len(rolling_sum)):
    if rolling_sum[i] > rolling_sum[i-1]:
        n_increase +=1

print(n_increase)
