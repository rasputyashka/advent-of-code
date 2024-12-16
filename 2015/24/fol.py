from itertools import permutations


sm = 0
rsum = 520
nums = []
for line in open(0).readlines():
    nums.append(int(line.strip()))

results = []
for p, i in enumerate(nums):
    for x in permutations(nums[p:], 3):
        if (sum(x)) == 390 - i:
            results.append(x+(i,))
minprod = 20000000000
for x in results:
    cur_prod = 1
    for y in x:
        cur_prod *= y
    minprod = min(minprod, cur_prod)
print(minprod)
