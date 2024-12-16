x = input()
ans = 0
for i in range(len(x)):
    if x[i] == x[(i+len(x)//2) % len(x)]:
        ans += int(x[i])
print(ans)
