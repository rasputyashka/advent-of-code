import re

def read():
    return [i.strip() for i in open(0)]
lines = read()

replacements = []
for i in lines[:-2]:
    m = re.findall(r'(\S+) => (\S+)', i)
    replacements.append(m[0])
X = lines[-1]

def f(X):
    for j, i in replacements:
        for k in range(len(X)):
            if X[k:k+len(i)] == i:
                y = X[:k] + j + X[k+len(i):]
                yield y

visited = {X}
m = [X]

replacements = sorted(replacements, key=lambda x: -len(x[1]))

visited = {X}
m = [X]

C = 0
while True:
    mm = []
    for i in m:
        for j in f(i):
            if j in visited:
                continue
            mm.append(j)
            visited.add(j)
            break # the only change
    m = mm
    C += 1
    print(C, len(m), min([len(x) for x in m], default=0), flush=True)

