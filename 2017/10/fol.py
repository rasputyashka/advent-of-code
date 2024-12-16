from __future__ import annotations
from dataclasses import dataclass
from functools import reduce

lst = list(range(int(input())))
lens = [ord(x) for x in input()] + [17, 31, 73, 47, 23]

def play_round():

    curpos = 0
    shift = 0
    for _ in range(64):
        for length in lens:

            if len(lst) - (curpos+length) >= 0:
                lst[curpos:curpos+length] = reversed(lst[curpos:curpos+length])
            else:
                indexes = [(curpos+i)%len(lst) for i in range(length)]
                values = [lst[idx] for idx in indexes]
                values = list(reversed(values))
                for pos, idx in enumerate(indexes):
                    lst[idx] = values[pos]
            curpos += length + shift
            shift += 1
        print(lst)
play_round()

for i in range(len(lst) // 16):
    s = i * 16
    res = reduce(lambda x, y: x^y, lst[s:s+16])
    print(f"{hex(res)[2:]:0>2}", end='')

