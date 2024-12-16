from itertools import permutations

lines = open(0).read().split("\n")


def scramble(string):
    for line in lines:
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
            case ["rotate", "right", x, "step"|"steps"]:
                for _ in range(int(x)):
                    string = [string[-1]] + string[:-1]
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
                if x is not None and y is not None:
                    string[x:y+1] = string[y:x-1:-1]
                elif x is None:
                    string[:y+1] = string[y:None:-1]
                elif y is None:
                    pass
            case ["move", "position", x, "to", "position", y]:
                x = string.pop(int(x))
                string.insert(int(y), x)
    return string 

for x in permutations("abcdefgh"):
    if scramble(list(x)) == list("fbgdceah"):
        print(x)
        break

