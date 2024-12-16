grid = [[" " for x in range(50)] for _ in range(6)]
for line in open(0).readlines():
    line = line.strip()
    match line.split():
        case ["rect", dim]:
            w, h = [int(x) for x in dim.split('x')]
            for r in range(h):
                for c in range(w):
                    grid[r][c] = "#"
        case ["rotate", "row", row, "by", val]:
            row_num = int(row.split("=")[-1])
            val = int(val)
            row = grid[row_num]
            row = row[-val:] + row[:-val]
            grid[row_num] = row
        case ["rotate", "column", column, "by", val]:
            column_num = int(column.split("=")[-1])
            val = int(val)
            column = [x[column_num] for x in grid]
            column = column[-val:] + column[:-val]
            for pos, el in enumerate(column):
                grid[pos][column_num] = el
cnt = 0
for x in grid:
    print(*x, sep="")
