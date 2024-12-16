res = 0
for line in open(0).read().splitlines():
    a, b, c = map(int, line.split("x"))
    res += a * b * c
    v = sorted([a, b, c])
    res += 2 * v[0] + 2 * v[1]
print(res)
