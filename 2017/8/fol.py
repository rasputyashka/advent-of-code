from collections import defaultdict

registers = defaultdict(int)
cur_max = 0
for line in open(0).readlines():
    line = line.strip()
    line = line.replace("inc", "+=")

    line = line.replace("dec", "-=")
    lregname = line.split()[0]
    if lregname not in registers:
        registers[lregname] = 0
    rregname = line.split()[-3]
    if rregname not in registers:
        registers[rregname] = 0
    ifstart = line.find("if ")
    new_line = line[ifstart:] + ": " + line[:ifstart]
    line = new_line.split()
    line[1] = f"registers['{line[1]}']"
    line[-3] = f"registers['{line[-3]}']"
    command = " ".join(line)
    exec(command)
    cur_max = max(max(registers.values()), cur_max)
print(cur_max)
