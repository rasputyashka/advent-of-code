from math import isqrt, sqrt
def sum_divisors(num):
    sm = 0
    if sqrt(num).is_integer():
        sm -= isqrt(num)
    for d in range(1, isqrt(num)+1):
        if num % d == 0:
            if d * 50 >= num:
                sm += d
            if num // d * 50 >= num:
                sm += num // d
    return sm

if __name__ == "__main__":
    for i in range(100000, 100000000):
        if sum_divisors(i) >= 3090910:
            print(i)
            break
