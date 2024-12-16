numbers = [int(x) for x in open(0).read().split()]

confs = {}

cnt = 0
while True:
    start_idx = numbers.index(max(numbers))
    mx_value = max(numbers)
    numbers[start_idx] = 0
    for _ in range(mx_value):
        start_idx += 1
        start_idx %= len(numbers)
        numbers[start_idx] += 1
    new_conf = tuple(numbers)
    if new_conf in confs:
        cnt += 1
        break
    cnt += 1
    confs[new_conf] = cnt
print(cnt - confs[new_conf])
