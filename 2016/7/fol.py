def get_reversed(a, b):
    return a+b+b+a

def determine(string):
    for pos, el in enumerate(string[:len(string)-1]):
        if len(set(string[pos:pos+4])) == 2:
            if string[pos:pos+4] == get_reversed(string[pos], string[pos+1]):
                return True
    return False


cnt = 0

def parse_string(string):
    in_b = []
    outside_b = []
    res = ""
    in_bracket = False
    for c in string:
        res += c
        if c == "[":
            outside_b.append(res[:-1])
            res = ""
            in_bracket = True
        if c == "]":
            in_b.append(res[:-1])
            res = ""
            in_bracket = False
    outside_b.append(res)
    return in_b, outside_b

for line in open(0).readlines():
    inside, outside = parse_string(line.strip())
    supports = False
    for word in outside:
        if determine(word):
            supports = True
    for word in inside:
        if determine(word):
            supports = False
    if supports:
        cnt += 1
print(cnt)
