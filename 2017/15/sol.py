rem = 2147483647

def ag():
    startval = 883
    mul = 16807
    while True:
        startval *= 16807
        startval %= rem
        if startval % 4 == 0:
            yield startval

def bg():
    startval = 879
    while True:
        startval *= 48271
        startval %= rem
        if startval % 8 == 0:
            yield startval


ga = iter(ag())
gb = iter(bg())

cnt = 0

for _ in range(5*10**6):
    a = next(ga)
    b = next(gb)

    if (a & 0xFFFF) == (b & 0xFFFF):
        cnt += 1

print(cnt)
