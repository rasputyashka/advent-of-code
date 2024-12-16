instructions = """jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
end""".split("\n")

a = 1
b = 0
idx = 0
while instructions[idx] != "end":
    instruction = instructions[idx]
    match instruction.split():
        case ["hlf", register]:
            a //= 2
            idx += 1
            continue
        case ["tpl", register]:
            a *= 3
            idx += 1
            continue
        case ["inc", register]:
            if register == "a":
                a += 1
            else:
                b += 1
            idx += 1
            continue
        case ["jmp", offset]:
            print(idx, offset, instruction)
            idx += int(offset)
            print(idx, offset, instruction)
            continue
        case ["jie", register, offset]:
            if a % 2 == 0:
                idx += int(offset)
            else:
                idx += 1
            continue
        case ["jio", register, offset]:
            if a == 1:
                idx += int(offset)
            else:
                idx += 1
            continue
        case _:
            print("WA", instruction)
print(b)
