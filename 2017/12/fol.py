from collections import defaultdict, deque

mapping = defaultdict(set)
cnt = 0
visited = set()
for line in open(0).readlines():
    units = line.strip().split()
    gid1 = int(units[0])
    gid2_list = "".join(units[2:]).split(",")
    for gid2 in gid2_list:
        mapping[gid1].add(int(gid2))
        mapping[int(gid2)].add(gid1)
print(mapping)

result = set()
for group_id in mapping:
    visited = set()
    queue = deque()
    queue.append(group_id)
    while queue:
        curnode = queue.popleft()
        visited.add(curnode)
        for node in mapping[curnode]:
            if node not in visited:
                queue.append(node)
    result.add(frozenset(visited))
print(len(result))
