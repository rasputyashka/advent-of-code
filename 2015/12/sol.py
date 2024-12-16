import re

data = input()
x = sum([int(x) for x in re.findall(r'-?\d+', data)])
print(x)
