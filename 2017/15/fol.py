a = 883
b = 879

#a = 65
#b = 8921

afac = 16807
bfac = 48271

rem = 2147483647

cnt = 0

REPS = 40*10**6

for power in range(REPS):
    a = a * afac % rem
    b = b * bfac % rem
    
    if (a & 0xFFFF) == (b & 0xFFFF):
        cnt += 1

print(cnt)
