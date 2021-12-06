import copy

# in_file = 'd6_test_in.txt'
in_file = 'd6_in.txt'
data = [line.rstrip('\n').split(',') for line in open(in_file)]
# print(data)
data = [int(i) for i in data[0]]
# print(data)

fish = [0]*9
for i in range(9):
    fish[i] = data.count(i)
# print(fish)

for i in range(256):
    new_fish = [0]*9
    for j in range(8,0,-1):
        new_fish[j-1] = copy.deepcopy(fish[j])
    new_fish[6] += fish[0]
    new_fish[8] = copy.deepcopy(fish[0])
    fish = copy.deepcopy(new_fish)
    # print(fish)
print(sum(fish))
