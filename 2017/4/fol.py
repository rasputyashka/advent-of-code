
cnt = 0
for line in open(0).readlines():
    if line:
        st = {frozenset(x) for x in line.split()}
        if len(st) == len(line.split()):
            cnt += 1
print(cnt)

