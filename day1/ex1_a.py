# in_file = 'd1_test_in.txt'
in_file = 'd1_a_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

data = [int(i) for i in data]

n_increase = 0
for i in range(1,len(data)):
    if data[i] > data[i-1]:
        n_increase +=1

print(n_increase)
