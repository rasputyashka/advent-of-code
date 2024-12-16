lst = []
for line in open(0).readlines():
    if line:
        lst.append(int(line))

idx = 0
cnt = 0
while idx < len(lst):
    cnt += 1
    cur_el = lst[idx]
    if cur_el > 2:
        lst[idx] -= 1
    else:
        lst[idx] += 1
    idx += cur_el
print(lst)
print(cnt)
