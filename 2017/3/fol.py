from math import isqrt

for i in range(26):
    print(i, end=" ")
    print(isqrt(i) -2  + (i % 2 != 0))

