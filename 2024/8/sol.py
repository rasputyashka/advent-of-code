from collections import defaultdict
from itertools import combinations
from pprint import pprint

data = [list(row.strip()) for row in open(0).readlines()]

antennas_positions = defaultdict(list)

for pr, r in enumerate(data):
    for pc, c in enumerate(r):
        if c != '.':
            antennas_positions[c].append(pr + 1j*pc)

antinodes = set()

for v in antennas_positions.values():
    for a, b in combinations(v, 2):
        dist = b-a
        b_antinode = b + dist
        a_antinode = a - dist

        if b_antinode.real in range(len(data)) and b_antinode.imag in range(len(data[0])):
            antinodes.add(b_antinode)
        if a_antinode.real in range(len(data)) and a_antinode.imag in range(len(data[0])):
            antinodes.add(a_antinode)

print(len(antinodes))
