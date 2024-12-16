
from collections import deque
from string import ascii_lowercase

d = deque(ascii_lowercase[:16])
instructions = open(0).read().split(',')

ans_d = d.copy()

for i in range(49):
    old_d = d.copy()
    for instr in instructions:
        if instr[0] == 's':
            d.rotate(int(instr[1:]))
        elif instr[0] == 'x':
            a, _, b = instr[1:].partition('/')
            a = int(a)
            b = int(b)
            d[a], d[b] = d[b], d[a]
        elif instr[0] == 'p':
            a = d.index(instr[1])
            b = d.index(instr[3])
            d[a], d[b] = d[b], d[a]
    if d == ans_d:
        print("GOTCHA", i)
    print(i, end=' ')
    print(*d, sep='')


