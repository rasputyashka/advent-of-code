import re
from collections import Counter
from string import ascii_lowercase as alphabet


number = re.compile(r'\d+')
checksum = re.compile(r'\[\w+\]')
sm = 0

for line in open(0).readlines():
    line = line.strip()
    cnumber = number.findall(line)[0]
    stop = line.find(cnumber)
    cnumber = int(cnumber)
    given_checksum = checksum.findall(line)[0][1:-1]
    mapping = Counter("".join(x for x in line[:stop] if x != '-'))
    common = mapping.items()
    tmp = sorted(common, key=lambda x: x[0])
    tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
    real_checksum = ''.join([x[0] for x in tmp])
    if real_checksum[:5] == given_checksum:
        sm += cnumber

    # pt 2
    res_string = ""
    for c in line[:stop-1]:
        res_string += alphabet[(alphabet.find(c) + cnumber) % 26]
    print(res_string, cnumber)
print(sm)
