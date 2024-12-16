from math import log2
from collections import defaultdict, Counter

nums = []
for line in open(0).readlines():
    line = line.strip()
    num = int(line)
    nums.append(num)


counter = Counter()
bits = defaultdict(int, enumerate(nums))
for i in range(2**len(nums)):
    sm = 0
    i = str(bin(i))[2:].zfill(len(nums))
    for pos, el in enumerate(i):
        if el == "1":
            sm += bits[pos]
    if sm == 150:
        counter[i.count('1')] += 1
print(counter[min(counter)])

