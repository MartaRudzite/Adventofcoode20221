# in_file = 'd8_test_in.txt'
in_file = 'd8_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

output_values = [i.split('|')[1].lstrip().split(' ') for i in data]
# print(output_values)

total = 0

for line in output_values:
    for digit in line:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            total +=1
            # print(digit)

print(total)
