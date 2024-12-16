import re

number_pattern = re.compile(r"\d+")
nums = [[0 for _ in range(1000)] for _ in range(1000)]

for line in open(0):
    sr, sc, er, ec = map(int, re.findall(number_pattern, line))
    words = line.split()
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if words[0] == "toggle":
                nums[r][c] += 2
            if words[1] == "on":
                nums[r][c] += 1
            if words[1] == "off":
                nums[r][c] = max(0, nums[r][c] - 1)

t = 0
for a in nums:
    t += sum(a)
print(t)
