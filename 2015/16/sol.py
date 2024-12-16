
sues = {}
sue = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}
for line in open(0).readlines():
    line = line.strip()
    num = line.split(" ")[1]
    line = line[line.find(':')+2:].split(', ')
    for unit in line:
        item, value = unit.split(": ")
        value = int(value)
        if item in ["cats", "trees"]:
            if value <= sue[item]:
                break
        elif item in ["pomeranians", "goldfish"]:
            if value >= sue[item]:
                break
        elif value != sue[item]:
            break
    else:
        print(num)
