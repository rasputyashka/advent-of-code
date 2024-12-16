from collections import defaultdict

initial = defaultdict(list)
instructions = defaultdict(dict)
outs = defaultdict(list)

import re

for line in open(0).readlines():
    units = line.split()
    if line.startswith("v"):
        initial[units[5]].append(int(units[1]))
    else:
        instructions[units[1]]["low"] = " ".join(units[5:7])
        instructions[units[1]]["high"] = " ".join(units[-2:])
while True:
    initial_copy = initial.copy()
    met_2 = False
    for v in initial_copy.values():
        if len(v) > 1:
            met_2 = True
    if not met_2:
        break
    for k, v in initial_copy.items():
        if len(v) > 1:
            mn, mx = min(v), max(v)
            v.remove(mn)
            v.remove(mx)
            #if mn == 17 and mx== 61:
            #    print(k)
            #    print(outs)
            #    exit(0)
            min_to = instructions[k]["low"]
            if "output" in min_to:
                outs[min_to.split()[-1]].append(mn)
            else:
                initial[min_to.split()[-1]].append(mn)
            max_to = instructions[k]["high"]
            if "output" in max_to:
                outs[max_to.split()[-1]].append(mx)
            else:
                initial[max_to.split()[-1]].append(mx)
for x in outs:
    if int(x) in [0, 1, 2]:
        print(outs[x])
