import re

regexp = re.compile(r'([a-z])\1')
pas = input()

num = 0
pw = 27  # aaa != a, so we add zero like a = 1 and 0 = 0
d = ["a"] + [chr(x) for x in range(ord('a'), ord('z')+1)]

for pos, c in enumerate(pas[::-1]):
    num += pw**pos * (ord(c) - ord('a') + 1)

def get_str(num):
    ans = ""
    while num > 0:
        ans += d[num % pw]
        num //= pw
    return ans[::-1]

def check_3(string):
    b = iter(string)
    c = iter(string)
    next(b)
    next(c)
    next(c)
    for i, j, k in zip(string, b, c):
        if ord(i)+1 == ord(j) and ord(j)+1 == ord(k):
            return True
    return False

while True:
    num += 1
    str_num = get_str(num)
    print(str_num)
    if check_3(str_num):
        if not any(x in 'loi' for x in str_num):
            if len(re.findall(regexp, str_num)) >= 2:
                break
