
string = list("fbgdceah")
for line in open(0).readlines():
    line = line.strip()
    print(line)
    match line.split():
        case ["swap", "position", from_, "with", "position", to]:
            f = int(from_)
            to = int(to)
            string[f], string[to] = string[to], string[f]
        case ["swap", "letter", lf, "with", "letter", tf]:
            lfi = string.index(lf)
            tfi = string.index(tf)
            string[lfi], string[tfi] = string[tfi], string[lfi]
        case ["rotate", "left", x, "step"|"steps"]:
            for _ in range(int(x)):
                string = string[1:] + [string[0]]
                print(string)
        case ["rotate", "right", x, "step"|"steps"]:
            for _ in range(int(x)):
                string = [string[:-1]] + string[:-1]
        case ["rotate", "based", "on", "position", "of", "letter", x]:
            idx = string.index(x)
            if idx >= 4:
                idx += 1
            idx += 1
            for _ in range(int(idx)):
                string = [string[-1]] + string[:-1]
        case ["reverse", "positions", x, "through", y]:
            x = int(x) or None
            y = int(y) or None
            print("xyz")
            print(string)
            if x is not None and y is not None:
                string[x:y+1] = string[y:x-1:-1]
            elif x is None:
                string[:y+1] = string[y:None:-1]
            elif y is None:
                pass
            print(string)
        case ["move", "position", x, "to", "position", y]:
            x = string.pop(int(x))
            string.insert(int(y), x)
    print(string)
print(string)
