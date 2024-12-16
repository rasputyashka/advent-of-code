from collections import Counter

data = open(0).readlines()

left = []
right = []
for x in data:
    l, r = map(int, x.split())
    left.append(l)
    right.append(r)

sm = 0
right = Counter(right)
for a in left:
    sm += a * right.get(a, 0)

print(sm)
