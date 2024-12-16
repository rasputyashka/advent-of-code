from help import main
from collections import deque

keyword = input()
grid = []

for i in range(128):
    rowname = keyword + '-' + str(i)
    knot_hash = main(rowname)
    
    row = []
    for c in knot_hash:
        tetrade = bin(int(c, 16))[2:]
        tetrade = f"{tetrade:0>4}"
        row.extend(tetrade.replace('1', '#').replace('0', '.'))
    
    grid.append(row)

for row in grid[:3]:
    print(*row, sep='')

def check_move(move):
    if move.real >= 0 and move.real < 128:
        if move.imag >= 0 and move.imag < 128:
            r = int(move.imag)
            c = int(move.real)
            return grid[r][c] == '#'

def find_sector(sector_num):
    sector_parts = set()
    moves = deque()
    directions = [1j, -1j, 1, -1]
    for pr, r in enumerate(grid):
        try:
            pos = r.index('#')
        except ValueError:
            continue
        else:
            start = pr*1j + pos
            moves.append(start)
            break
    while moves:
        cur_move = moves.popleft()
        sector_parts.add(cur_move)
        for direction in directions:
            new_move = cur_move + direction
            if new_move not in sector_parts and check_move(new_move):
                moves.append(new_move)
    print(sector_parts)
    if not len(sector_parts):
        return -1
    for cord in sector_parts:
        r = int(cord.imag)
        c = int(cord.real)
        grid[r][c] = sector_num + 1
    print(grid[0])
    return sector_num + 1


sector_num = 0
while True:
    sector_num = find_sector(sector_num)
    if sector_num == -1:
        break
    else:
        print(sector_num)
