import re

numbers = re.compile(r"\d+")
nodes = []
cnt = 0

for line in open(0).readlines():
    nodes.append([cnt]+[int(x) for x in numbers.findall(line)])
    cnt += 1

ttl = 0

for i1, node1 in enumerate(nodes):
    for i2, node2 in enumerate(nodes):
        if i1 == i2:
            continue
        if node1[4] != 0:
            if node1[4] <= node2[5]:
                ttl += 1
print(ttl)
