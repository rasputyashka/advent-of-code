registers = {"a": 12}

commands = open(0).read().split("\n")
inum = 0
while inum < len(commands):
    line = commands[inum]
    print(line)
    if inum != 4:
        match line.split():
            case ["tgl", regname]:
                print("here")
                value = registers[regname]
                if value + inum < len(commands):
                    toggled_command = commands[value+inum]
                    splited = toggled_command.split()
                    if len(splited) == 2:
                        if "inc" in splited:
                            splited[0] = "dec"
                        else:
                            splited[0] = "inc"
                    elif len(splited) == 3:
                        if "jnz" in splited:
                            splited[0] = "cpy"
                        else:
                            splited[0] = "jnz"
                    commands[value+inum] = " ".join(splited)
                print(commands)
            case ["cpy", value, regname]:
                try:
                    if value.isdigit() or "-" in value:
                        registers[regname] = int(value)
                    else: registers[regname] = registers[value]
                except:
                    pass
            case ["inc", regname]:
                registers[regname] += 1
            case ["dec", regname]:
                registers[regname] -= 1
            case ["jnz", testreg, shift]:
                try:
                    shift = int(shift)
                except ValueError:
                    shift = registers[shift]
                if testreg.isdigit():
                    inum += int(shift)
                    continue
                else:
                    if registers[testreg] != 0:
                        inum += int(shift)
                        continue
        inum += 1
    else:
        registers["a"] = registers["b"] * registers["d"]
        registers["c"] = 0
        registers["d"] = 0
        inum = 10

print(registers["a"])
