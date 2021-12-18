in_file = 'd9_test_in.txt'
in_file = 'd9_in.txt'
data = [list(line.rstrip('\n')) for line in open(in_file)]
# print(data)
heatmap = []
row = [9]*(len(data[0])+2)
heatmap.append(row)
for line in data:
    row = [9]
    for i in line:
        row.append(int(i))
    row.append(9)
    heatmap.append(row)
row = [9]*(len(data[0])+2)
heatmap.append(row)

# for line in heatmap:
#     print(line)

# print(len(heatmap))
risk = 0
for i in range(1,len(heatmap)-1):
    for j in range(1,len(heatmap[0])-1):
        if (heatmap[i][j] < heatmap[i-1][j] and
            heatmap[i][j] < heatmap[i][j-1] and
            heatmap[i][j] < heatmap[i+1][j] and
            heatmap[i][j] < heatmap[i][j+1] ):
            risk += heatmap[i][j] + 1
            # print(i,j)
print(risk)
