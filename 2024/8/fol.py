
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
        antinodes.add(a)
        antinodes.add(b)
        while b_antinode.real in range(len(data)) and b_antinode.imag in range(len(data[0])):
            antinodes.add(b_antinode)
            b_antinode += dist

        while a_antinode.real in range(len(data)) and a_antinode.imag in range(len(data[0])):
            antinodes.add(a_antinode)
            a_antinode -= dist

for x in antinodes:
    data[int(x.real)][int(x.imag)] = '#'

print(len(antinodes))
