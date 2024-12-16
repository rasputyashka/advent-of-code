data = input().split(",")
pos = 0

s = r = q = 0
curmax = 0
for c in data:
    if c == "s":
        r += 1
        s -= 1
    elif c == "n":
        r -= 1
        s += 1
    elif c == "ne":
        q += 1
        r -= 1
    elif c == "nw":
        q -= 1
        s += 1
    elif c == "se":
        s -= 1
        q += 1
    elif c == "sw":
        r += 1
        q -= 1
    curmax = max(curmax, (abs(r) + abs(q) + abs(s)) // 2)
print(curmax)
