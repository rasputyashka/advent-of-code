from collections import deque

FAVOURITE_NUM = 1364

def get_being(num: complex):
    x, y = int(num.real), int(num.imag)
    entity = (x+y) ** 2 + 3*x + y + FAVOURITE_NUM
    return "." if bin(entity).count("1") % 2 == 0 else "#"
start = 1+1j

moves = [
    1,
    -1,
    1j,
    -1j,
]

DESIRED_COORDS = 31+39j

queue = deque()
queue.append((start, 0))
visited_coords = set()
while queue:
    coords, distance = queue.popleft()
    print(coords)
    visited_coords.add(coords)
    if distance >= 50:
        continue
    else:
        for move in moves:
            proposed = coords + move
            if proposed not in visited_coords:
                if proposed.imag < 0 or proposed.real < 0:
                    continue
                else:
                    if get_being(proposed) == ".":
                        queue.append((proposed, distance+1))
print(len(visited_coords))
