registers = {"a": 0, "b": 0, "c": 1, "d": 0}

commands = open(0).read().split("\n")
inum = 0
while inum < len(commands):
    line = commands[inum]
    match line.split():
        case ["cpy", value, regname]:
            if value.isdigit():
                registers[regname] = int(value)
            else: registers[regname] = registers[value]
        case ["inc", regname]:
            registers[regname] += 1
        case ["dec", regname]:
            registers[regname] -= 1
        case ["jnz", testreg, shift]:
            if testreg.isdigit():
                inum += int(shift)
                continue
            else:
                if registers[testreg] != 0:
                    inum += int(shift)
                    continue
    inum += 1
print(registers["a"])
