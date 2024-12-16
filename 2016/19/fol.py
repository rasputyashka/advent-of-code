#a = list(range(1, int(input())+1))
#while len(a) != 1:
#    last = a[-1]
#    a = a[::2]
#    if a[-1] == last:
#        a = [a[-1]] + a[:-1]
#    print(a)
#print(a)

# another solution is much simplier

x = bin(int(input()))[2:]
x = x[1:] + x[-1]
print(int(x, 2))
