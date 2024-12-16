from collections import Counter

lst = [Counter() for x in range(8)]

for line in open(0).readlines():
    line = line.strip()
    for i in range(8):
        lst[i][line[i]] += 1

for x in lst:
    print(x.most_common()[::-1][0][0], end="")
