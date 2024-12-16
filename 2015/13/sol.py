from collections import defaultdict
from itertools import permutations, pairwise
from pprint import pprint as print

d = defaultdict(dict)

for line in open(0).readlines():
    units = line.split()
    from_ = units[0]
    sign = -1 if units[2] == "lose" else 1
    value = int(units[3]) * sign
    to = units[-1][:-1]
    opposite = d[to].get(from_, 0)
    d[from_][to] = value + opposite
    d[to][from_] = value + opposite
    d[from_]["me"] = 0
    d["me"][from_] = 0
# you can try to measurue the magnitude of pairs like A + B, C + D, C + A etc instead of having 2n dict
maxval = 0
sitting = None
for all_places in permutations(d, len(d)):
    sm = 0
    for l, r in pairwise(all_places):
        sm += d[l][r]
    sm += d[all_places[0]][all_places[-1]]
    if sm >= maxval:
        maxval = sm
        sitting = all_places
print(all_places)
print(maxval)
