cnt = 0
weight = 0

line = input()
brackets = []

idx = 0
prev_garb = 0
total_garb = 0
while idx < len(line):
    c = line[idx]
    if c == "!":
        idx += 2
        prev_garb += 2
        continue
    elif c == "<":
        if not brackets or brackets[-1] != "<":
            prev_garb = idx
            brackets.append(c)
    elif c == "{":
        if not brackets or brackets[-1] != "<":
            brackets.append(c)
    elif c == "}":
        if brackets and brackets[-1] == "{":
            brackets.pop()
            cnt += 1
    elif c == ">":
        if brackets and brackets[-1] == "<":
            total_garb += idx - prev_garb - 1
            brackets.pop()
    idx += 1
print(total_garb)
