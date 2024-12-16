
def get_reversed(a, b):
    return a+b+b+a


def determine(string, outs):
    for a, b, c in zip(string, string[1:], string[2:]):
        if a == c and a != b:
            for word in outs:
                if b + a + b in word:
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
        if determine(word, inside):
            supports = True
    if supports:
        cnt += 1
print(cnt)
