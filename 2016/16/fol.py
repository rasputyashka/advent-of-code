def exec_steps(a):
    b = "".join(str(int(c != "1")) for c in a[::-1])
    return a + "0" + b

def get_checksum(a, size):
    while len(a) < size:
        a = exec_steps(a)
    a = a[:size]
    while len(a) % 2 == 0:
        new_a = ""
        for i in range(0, len(a)-1, 2):
            c, b = a[i], a[i+1]
            new_a += str(int(c==b))
        print(new_a)
        a = new_a
    return a

print(get_checksum("10111011111001111", 35651584))

