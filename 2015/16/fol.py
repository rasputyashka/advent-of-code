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
    a, b, c = line
    ad, av = a.split(': ')
    bd, bv = b.split(': ')
    cd, cv = c.split(': ')

    av = int(av)
    bv = int(bv)
    cv = int(cv)

    
