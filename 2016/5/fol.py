inpt = "ugkcyxxp"
idx = 0

from hashlib import md5

res = [0]*8

string = ""

while len(string) != 8:
    while not md5((inpt+str(idx)).encode('utf-8')).hexdigest().startswith("00000"):
        idx += 1
    hashh = md5((inpt+str(idx)).encode("utf-8")).hexdigest()
    pos = hashh[5]
    print(idx, flush=True)
    if pos.isdigit() and int(pos) < 8:
        if not res[int(pos)]:
            res[int(pos)] = hashh[6]
            string += " "
    idx += 1
print(res)
