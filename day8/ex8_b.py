# in_file = 'd8_test_in.txt'
in_file = 'd8_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

input_values = [i.split('|')[0].rstrip().split(' ') for i in data]
output_values = [i.split('|')[1].lstrip().split(' ') for i in data]

sum = 0

for idx, line in enumerate(input_values):
    number_key = [0]*10
    numbers = sorted(line, key=len)
    number_key[1] = ''.join(sorted(numbers[0]))
    number_key[7] = ''.join(sorted(numbers[1]))
    number_key[4] = ''.join(sorted(numbers[2]))
    number_key[8] = ''.join(sorted(numbers[9]))
    for i in [3,4,5]:
        key_i = ''.join(sorted(numbers[i]))
        if len(set(number_key[1]) & set(key_i)) == 2:
            number_key[3] = key_i
        elif len(set(number_key[4]) & set(key_i)) == 2:
            number_key[2] = key_i
        elif len(set(number_key[4]) & set(key_i)) == 3:
            number_key[5] = key_i
        else:
            print('2-3-5 seperation is not working')
    for i in [6,7,8]:
        key_i = ''.join(sorted(numbers[i]))
        if len(set(number_key[4]) & set(key_i)) == 4:
            number_key[9] = key_i
        elif len(set(number_key[5]) & set(key_i)) == 5:
            number_key[6] = key_i
        else:
            number_key[0] = key_i
    # print(number_key)

    numbers_idx = []
    for i in output_values[idx]:
        numbers_idx.append(number_key.index(''.join(sorted(i))))
    # print(numbers_idx)
    sum += int(''.join(str(i) for i in numbers_idx))
    # print(sum)

print(sum)
