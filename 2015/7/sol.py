from operator import *
from collections import deque

x = deque()
values = {}

for line in open(0):
    line = line.strip()
    tokens = line.split()
    if len(tokens) == 3:
        if tokens[0].isdigit():
            if tokens[-1] == "b":
                values[tokens[-1]] = 16076
            else:
                values[tokens[-1]] = int(0)
        else:
            x.append(tokens)
    else:
        x.append(tokens)

while x:
    expr = x.popleft()
    print(expr)
    match expr:
        case ["NOT", left, _, dest]:
            if left.isdigit():
                values[dest] = ~int(left)
            if left in values:
                values[dest] = ~values[left]
            else:
                x.append(expr)
        case [left, "RSHIFT", right, _, dest]:
            if left in values:
                right = int(right)
                values[dest] = values[left] >> right
            else:
                x.append(expr)
        case [left, "LSHIFT", right, _, dest]:
            if left in values:
                right = int(right)
                values[dest] = values[left] << right
            else:
                x.append(expr)
        case [str(left), "AND", str(right), _, str(dest)]:
            if left.isdigit():
                left = int(left)
                if right.isdigit():
                    # print(1)
                    # print(values)
                    values[dest] = left & int(right)
                else:
                    # print(2)
                    # print(values)
                    if right in values:
                        values[dest] = left & values[right]
                    else:
                        x.append(expr)
            else:
                if right.isdigit():
                    right = int(right)
                elif left in values and right in values:
                    values[dest] = values[left] & values[right]
                else:
                    x.append(expr)
        case [str(left), "OR", str(right), _, str(dest)]:
            if left.isdigit():
                left = int(left)
                if right.isdigit():
                    values[dest] = left | int(right)
                else:
                    if right in values:
                        values[dest] = left | values[right]
                    else:
                        x.append(expr)
            else:
                if right.isdigit():
                    right = int(right)
                elif left in values and right in values:
                    values[dest] = values[left] | values[right]
                else:
                    x.append(expr)
        case [left, "->", right]:
            if left in values:
                values[right] = values[left]
            else:
                x.append(expr)

print(values["a"])
