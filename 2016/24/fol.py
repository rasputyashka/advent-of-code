from collections import deque
from itertools import combinations, permutations
grid = []

places = {}
cnt = 0
power = 0
for line in open(0).readlines():
    line = line.strip()
    grid.append(line)
    for pos, c in enumerate(line):
        if c == "0":
            start = pos + cnt*1j
            places[int(c)] = pos + cnt*1j
        elif c.isdigit():
            power = max(power, int(c))
            places[int(c)] = pos + cnt*1j
    cnt += 1
moves = [-1, 1j, -1j, 1]

def find_min(a, b):
    visited = set()
    queue = deque()
    queue.append((a, 0))
    while queue:
        start, dist = queue.popleft()
        visited.add(start)
        c = int(start.real)
        r = int(start.imag)
        if start == b:
            return dist
        for move in moves:
            new_move = move + start
            c = int(new_move.real)
            r = int(new_move.imag)
            next_el = grid[r][c]
            if next_el in "." and new_move not in visited:
                queue.append((new_move, dist+1))
            elif next_el in "0123456789":
                if new_move == b:
                    return dist+1
                else:
                    continue
print(places)
distances = {
    0: {2: 44, 1: 28, 3: 224, 4: 188, 5:148, 6: 212, 7: 76},
    1: {5: 136, 0: 28, 2: 60, 3: 212, 4: 176, 6: 200, 7: 92},
    2: {0: 44, 1: 60, 7: 36},
    3: {0: 224, 1: 212, 4: 48, 6: 64, 5: 84},
    4: {0: 188, 1: 176, 3: 48, 5: 48, 6: 40},
    5: {1: 136, 6: 72, 0: 148, 3: 84, 4: 48, 7: 200},
    6: {0: 212, 1: 200, 4: 40, 5: 72, 3: 64},
    7: {2: 36, 0: 76, 1: 92, 5: 200}
}

a, b = places[3], places[2]
print(find_min(a, b))
minpath = 20000000
for x in permutations("1234567"):
    path = distances[0][int(x[0])]
    flag = False
    for a, b in zip(x, x[1:]):
        a = int(a)
        b = int(b)
        if b in distances[a]:
            path += distances[a][b]
        else:
            flag = True
            break
    path += distances[b][0]
    if not flag:
        minpath = min(path, minpath)
print(minpath)
