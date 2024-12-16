cur = 0 + 0j
s = [1j, 1, -1j, -1]
cs = 0
visited = set()
for x in open(0).read().split(", "):
    d, c = x[0], x[1:]
    f = 1 if d == "R" else -1
    cs += f
    cs %= 4
    for i in range(1, int(c)+1):
        cur += s[cs]
        if cur in visited:
            print(cur)
            exit(0)
        visited.add(cur)
