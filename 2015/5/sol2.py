cnt = 0
for line in open(0):
    line = line.strip()

    ac = False
    bc = False

    l = ""
    r = ""
    for i in range(len(line)):
        if not ac and line[i : i + 2] in line[i + 2 :]:
            ac = True
            break
    for i in range(len(line) - 2):
        if line[i] == line[i + 2] and line[i + 1] != line[i]:
            bc = True
            break
    if ac and bc:
        cnt += 1
print(cnt)
