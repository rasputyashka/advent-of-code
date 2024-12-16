grid = [[0]*102]
W = 0
H = 0
for line in open(0).readlines():
    line = line.strip()
    tmp = [0]
    tmp += [(char == "#")*1 for char in line]
    tmp += [0]
    grid.append(tmp)
    H += 1
W = len(grid[2])-1
grid += [[0]*102]

shifts = [
    -1-1j,
    -1j,
    1-1j,
    -1+0j,
    1+0j,
    -1 + 1j,
    1j,
    1 + 1j
]
for i in range(100):
    to_zeros = set()
    to_ones = set()
    for r in range(1, H+1):
        for c in range(1, W):
            cnt = 0
            cur_el = grid[r][c]
            for shift in shifts:
                sc = shift.real
                sr = shift.imag
                cnt += grid[int(r+sr)][int(c+sc)]
            if cur_el == 1 and cnt not in [2, 3]:
                to_zeros.add((r, c))
            elif cur_el == 0 and cnt == 3:
                to_ones.add((r, c))
    for (r, c) in to_zeros:
        grid[r][c] = 0
    for (r, c) in to_ones:
        grid[r][c] = 1
res = 0
for r in grid:
    for c in r:
        res += c
print(res)