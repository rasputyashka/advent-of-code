cnt = 0
for line in open(0).readlines():
    if line:
        if len(line.split()) == len(set(line.split())):
            cnt += 1
print(cnt)

