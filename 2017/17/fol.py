from collections import deque

steps = 382
length = 1
init_pos = 0
ans = 0

for _ in range(1, 50000001):
    init_pos = (init_pos + steps) % length + 1
    if init_pos == 1:
        ans = _
    length += 1

print(ans)
