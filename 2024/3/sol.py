import re

pattern = re.compile(r'mul\((\d+),(\d+)\)')

sm = 0
inpt = input()
while 'don\'t()' in inpt:
    dont_index = inpt.index("don't")
    inpt = inpt[:dont_index] + inpt[inpt.index('do()', dont_index):]
    
for x in pattern.findall(inpt):
    sm += int(x[0]) * int(x[1])
print(sm)
