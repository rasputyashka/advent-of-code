from collections import deque
from hashlib import md5

def isopen(letter):
    return letter in "bcdef"

salt = input()
start = 1+1j
queue = deque()
queue.append((salt, start, ""))
visited = set()

maxstring = ""

while queue:
    salt, coords, path = queue.popleft()
    ghash = md5(salt.encode("utf8")).hexdigest()
    print(coords)
    print(ghash)
    if coords == 4 + 4j:
        if len(path) > len(maxstring):
            maxstring = path
        print(path)
        continue
    u, d, l, r = ghash[:4]
    if isopen(u): print("up")
    if isopen(d): print("down")
    if isopen(l): print("left")
    if isopen(r): print("right")
    if isopen(u) and coords.imag >= 2:
        queue.append((salt+"U", coords-1j, path+"U"))
    if isopen(d) and coords.imag <= 3:
        queue.append((salt+"D", coords+1j, path+"D"))
    if isopen(l) and coords.real >= 2:
        queue.append((salt+"L", coords-1, path+"L"))
    if isopen(r) and coords.real <= 3:
        queue.append((salt+"R", coords+1, path+"R"))
print(len(maxstring))
