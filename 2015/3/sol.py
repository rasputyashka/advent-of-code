x = 0 + 0j
visited = {x}

m = {
    ">": 1,
    "<": -1,
    "^": 1j,
    "v": -1j,
}

d = input()
for c in d[1::2]:
    x += m[c]
    visited.add(x)

x = 0 + 0j
for c in d[::2]:
    x += m[c]
    visited.add(x)

print(len(visited))
