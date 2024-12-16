rs = 0
for line in open(0).readlines():
    lst = sorted([int(x) for x in line.strip().split()])
    for p1, a in enumerate(lst):
        for p2, b in enumerate(lst[p1+1:]):
            if a % b == 0:
                print(a, b)
                rs += a // b
            elif b % a == 0:
                print(a, b)
                rs += b // a
print(rs)
