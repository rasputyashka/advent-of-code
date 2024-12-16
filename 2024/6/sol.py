from pprint import pprint

grid = [list(row.strip()) for row in open(0).readlines()]

for pr, r in enumerate(grid):
    for pc, c in enumerate(r):
        if c == '^':
            curpos = pc + 1j * pr
            break

dirchar = 'U'
directions = {'U': -1j, 'D': 1j, 'R': 1, 'L': -1}
curdir = directions[dirchar]

seen = {curpos, }


while 1:
    next_move = curpos + curdir
    try:
        if grid[int(next_move.imag)][int(next_move.real)] == '#':
            dirchar = 'URDL'[('URDL'.index(dirchar) + 1) % 4]
            curdir = directions[dirchar]
            next_move = curpos + curdir
        seen.add(curpos)
        curpos = next_move
    except IndexError:
        print(next_move)
        seen.add(curpos)
        break

print(len(seen))
