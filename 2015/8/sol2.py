import re

# lines = open("day8.txt", "r").read().split("\n")
lines = open(0).read().split("\n")
reg = re.compile(r"(\\)|(\")")
difference = 0

for line in lines:
    difference += len(reg.findall(line)) + 2
print(difference)
