ranges = []

for line in open(0).readlines():
    line = line.strip()
    a, b = line.split("-")
    a = int(a)
    b = int(b)
    ranges.append([a, b])

ranges.sort()

ranges = ranges
start_index = 0
res = []
while start_index < len(ranges):
    cur_range = ranges[start_index]
    for pos, el in enumerate(ranges[start_index:], start_index):
        if el[0] <= cur_range[1]+1:
            cur_range[1] = max(cur_range[1], el[1])
        else:
            res.append(cur_range)
            start_index = pos
            break
    else:
        res.append(cur_range)
        break
print(res)
cnt = 0
for i in range(len(res)-1):
    cnt += res[i+1][0]-res[i][1]-1
print(cnt)

