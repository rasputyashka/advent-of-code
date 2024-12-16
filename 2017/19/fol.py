from collections import deque
from string import ascii_uppercase as upc

paths = [line[:-1] for line in open(0).readlines()]
paths[0] = paths[0].ljust(len(paths[1]), ' ')

start = paths[0].index('|') + 0j

direction = 1j
q = deque()
q.append((start, direction, '', 1))

def check(move, lst):
    if 0 <= move.imag < len(lst) and 0 <= move.real < len(lst[0]):
        return True

def get_char(move, lst):
    return paths[int(move.imag)][int(move.real)]

while q:
    pos, direction, letters, steps = q.popleft()
    if get_char(pos, paths).isalpha():
        letters += get_char(pos,  paths)
    move = pos + direction
    while check(move, paths) and get_char(move, paths) not in [' ', '+']:
        if (letter := paths[int(move.imag)][int(move.real)]).isalpha():
            letters += letter
        move += direction
        steps += 1
    steps += 1
    print(steps)
    if paths[int(move.imag)][int(move.real)] == '+':
        probes = [1j, -1j, 1, -1]
        probes.remove(-direction)
        probes.remove(direction)
        for probe in probes:
            new_move = move + probe
            if check(new_move, paths) and (x := get_char(new_move, paths)) != ' ':
                q.append((new_move, probe, letters, steps+1))
                break
    else:
        print(steps-1)
