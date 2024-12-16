def solve(num):
    lst = list(range(1, num+1))
    idx = 0
    while len(lst) != 1:
        lst.pop((idx+len(lst)//2)%len(lst))
        idx += 1
        if idx >= len(lst):
            lst = [lst[-1]] + lst[:-1]
            idx = idx % len(lst)
    return lst[0]
#for IN in range(1, 7):
#    print(f"{IN:>2}: {solve(IN)}")
print(solve(3017957))
