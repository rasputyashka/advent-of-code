res = 0
for pos, c in enumerate(open(0).read()):
    res += 1 if c == "(" else -1
    if res == -1:
        print(pos + 1)
        exit(0)
