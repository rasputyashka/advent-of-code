from collections import deque

lst = [(int(x.split(': ')[0]), [int(y) for y in x.split(': ')[1].split()]) for x in open(0).readlines()]

sm = 0
for eq in lst:
    d = deque()
    res = eq[0]
    opts = eq[1]

    skip_eq = False
    d.append((opts[0] + opts[1], opts[2:], res))
    d.append((opts[0] * opts[1], opts[2:], res))
    d.append((int(str(opts[0]) + str(opts[1])), opts[2:], res))
    while d:
        value, opts, res = d.popleft()
        if opts:
            d.append((value + opts[0], opts[1:], res))
            d.append((value * opts[0], opts[1:], res))
            d.append((int(str(value) + str(opts[0])), opts[1:], res))
        elif value == res:
            skip_eq = True
            break
    if skip_eq:
        sm += res

print(sm)
