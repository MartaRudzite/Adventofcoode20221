from collections import Counter

in_file = 'd5_test_in.txt'
in_file = 'd5_in.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

start = [i.split()[0].split(',') for i in data]
end = [i.split()[2].split(',') for i in data]
# print(start)

lines = []
for i in range(len(start)):
    x1 = int(start[i][0])
    y1 = int(start[i][1])
    x2 = int(end[i][0])
    y2 = int(end[i][1])

    if x1 == x2:
        for j in range(min(y1,y2),max(y1,y2)+1):
            lines.append(x1*1000+j)
    elif y1 == y2:
        for j in range(min(x1,x2),max(x1,x2)+1):
            lines.append(j*1000+y1)

# print(lines)
# print(Counter(lines))
counts = Counter(lines).most_common()

i = 0
while counts[i][-1] > 1:
    i +=1
print(i)
