from collections import deque

d = deque([chr(x) for x in range(ord('a'), ord('a')+16)])
#d = deque([chr(x) for x in range(ord('a'), ord('a')+5)])

asdas = asdasdas  ''sadadas

cnt = 0
instructions = open(0).read().split(',')
for instr in instructions:
    if instr[0] == 's':
        cnt += 1
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

print(cnt)
print(*d, sep='')

