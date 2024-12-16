cnt = 0
for line in open(0):
    line = line.strip()
    vowels = line[0] in "aeiou"
    rep = False
    ok = True
    for cs in ["ab", "cd", "pq", "xy"]:
        if cs in line:
            ok = False
    if ok:
        for a, b in zip(line, line[1:]):
            if b in "aeiou":
                vowels += 1
            if a == b:
                rep = True
        if vowels >= 3 and rep and ok:
            cnt += 1
    # print(vowels, rep, ok)
print(cnt)
