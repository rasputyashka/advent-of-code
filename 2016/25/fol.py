commands = open(0).read().split("\n")

def solve(a):
    def gvalue(x):
        if x in registers:
            return registers[x]
        return int(x)

    registers = {"a": a}
    inum = 0
    out = []
    while len(out) != 1:
        if inum == 3:
            registers["d"] += registers["b"] * registers["c"]
            registers["b"] = 0
            inum = 6
            continue
        line = commands[inum]
        inum += 1
        match line.split():
            case ["out", _]:
                print(registers["b"])
                out.append(str(registers["b"]))
            case ["cpy", value, regname]:
                registers[regname] = gvalue(value)
            case ["inc", regname]:
                registers[regname] += 1
            case ["dec", regname]:
                registers[regname] -= 1
            case ["jnz", testreg, shift]:
                shift = int(shift)
                testreg = gvalue(testreg)
                if testreg != 0:
                    inum += shift - 1
solve(195)
