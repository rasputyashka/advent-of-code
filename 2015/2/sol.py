res = 0
for x in open(0).read().splitlines():

    a, b, c = map(int, x.split("x"))
    res += 2 * a * b + 2 * a * c + 2 * b * c
    v = sorted([a, b, c])
    res += v[0] * v[1]

print(res)
