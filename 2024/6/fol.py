
from pprint import pprint

grid = [list(row.strip()) for row in open(0).readlines()]

for pr, r in enumerate(grid):
    for pc, c in enumerate(r):
        if c == '^':
            startpos = pc + 1j * pr
            break

dirchar = 'U'
directions = {'U': -1j, 'D': 1j, 'R': 1, 'L': -1}

def get_local_path():
    seen = {startpos,}
    curpos = startpos
    curdir = directions['U']
    dirchar = 'U'
    while 1:
        next_move = curpos + curdir
        if next_move == 7+10j and len(grid) == 10 or next_move == 115+130j:
            break
        if grid[int(next_move.imag)][int(next_move.real)] == '#':
            dirchar = 'URDL'[('URDL'.index(dirchar) + 1) % 4]
            curdir = directions[dirchar]
            next_move = curpos + curdir
        seen.add(next_move)
        curpos = next_move
    return seen

cnt = 0
for x in get_local_path():
    j = int(x.imag)
    i = int(x.real)
    curpos = startpos
    before = grid[i][j]
    grid[i][j] = '#'
    curdir = directions['U']
    dirchar = 'U'

    seen = {(startpos, curdir), }
    while 1:
        next_move = curpos + curdir
        if (next_move.imag not in range(len(grid))) or (next_move.real not in range(len(grid[0]))):
            break
        if grid[int(next_move.imag)][int(next_move.real)] == '#':
            dirchar = 'URDL'[('URDL'.index(dirchar) + 1) % 4]
            curdir = directions[dirchar]
            next_move = curpos + curdir
        if (next_move, curdir) in seen:
            cnt += 1
            break
        seen.add((curpos, curdir))
        curpos = next_move
    grid[i][j] = before

print(cnt)
