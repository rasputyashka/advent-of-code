import hashlib

strng = input()

for i in range(2**1000):
    test = strng + str(i)
    if hashlib.md5(test.encode("utf-8")).hexdigest()[:6] == "000000":
        print(i)
        exit(0)
