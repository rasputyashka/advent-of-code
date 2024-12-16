from help import main

keyword = input()
grid = []

sm = 0

for i in range(128):
    rowname = keyword + '-' + str(i)
    knot_hash = main(rowname)
    
    row = []
    for c in knot_hash:
        tetrade = bin(int(c, 16))[2:]
        tetrade = f"{tetrade:0>4}"
        sm += tetrade.count('1')
        row.extend(tetrade)
    
    grid.append(row)

print(sm)
