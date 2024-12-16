a, b = int(input()), int(input())
res = (((a + b - 2) * (a + b - 1) // 2) + b) - 1
ans = 20151125
for _ in range(res):
    ans = ans * 252533 % 33554393
print(ans)
