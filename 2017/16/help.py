from collections import deque
from string import ascii_lowercase

#d = deque(ascii_lowercase[:16])
x = d.copy()

instructions = open(0).read().split(',')

def get_shifts(cur, prev):
    shifts = []
    for c in cur:
        shifts.append(prev.index(c))
    return shifts

cur_rotate = 0
rotates = []

for instr in instructions:
    if instr[0] == 's':
        cur_rotate += 1
        rotates.append((int(instr[1:]), get_shifts(d, x)))
        d.rotate(int(instr[1:]))
        x = d.copy()
    elif instr[0] == 'x':
        a, _, b = instr[1:].partition('/')
        a = int(a)
        b = int(b)
        d[a], d[b] = d[b], d[a]
    elif instr[0] == 'p':
        a = d.index(instr[1])
        b = d.index(instr[3])
        d[a], d[b] = d[b], d[a]

print(d, x)
rotates.append((0, get_shifts(d, x)))

d = deque('baedc')

for _ in range(1):
    for (a, b) in rotates:
        x = deque()
        print(a, b)
        d.rotate(a)
        for pos in b:
            x.append(d[pos])
        d = x.copy()
        print(x, d)

print(*d, sep='')

