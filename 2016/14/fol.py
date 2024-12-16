from hashlib import md5

salt = "yjdafjpo"
#salt = "abc"
idx = 0

proposed = []

ok = []

while len(ok) < 64:
    phash = md5((salt+str(idx)).encode("utf-8")).hexdigest()
    for i in range(2016):
        phash = md5(phash.encode("utf-8")).hexdigest()
    red_flag = False
    for (letter, index, pphash) in proposed:
        if idx - index > 1000:
            if index == 22034:
                print("outdated")
            proposed.remove((letter, index, pphash))
            red_flag = True
        elif letter*5 in phash:
            ok.append(index)
            red_flag = True
            proposed.remove((letter, index, pphash))
    if red_flag:
        continue
    for a1, a2, a3 in zip(phash, phash[1:], phash[2:]):
        if a1 == a2 == a3:
            proposed.append((a1, idx, phash))
            break
    if idx == 22034:
        print("are here", phash)
    idx += 1
print(sorted(ok))
print(sorted(ok)[63])
print(proposed)
print(len(ok))
