import re

number_pattern = re.compile(r"\d+")
nums = [0 for _ in range(1000)]

for line in open(0):
    sr, sc, er, ec = map(int, re.findall(number_pattern, line))
    words = line.split()
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if words[0] == "toggle":
                nums[r] ^= 1 << c
            if words[1] == "on":
                nums[r] |= 1 << c
            if words[1] == "off":
                nums[r] &= ~(1 << c)

total = 0

for number in nums:
    total += number.bit_count()

print(f"{total}")
