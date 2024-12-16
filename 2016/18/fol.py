#fr = input()
#count = int(input())

fr = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."
#count = 40

#  fr = ".^^.^.^^^^"
count = 400000-1
pvrow = "."+fr+"."
cnt = fr.count(".")
for _ in range(count):
    new_row = ""
    for pos, c in enumerate(pvrow[1:-1], 1):
        if c == "^" and pvrow[pos-1] == "^" and pvrow[pos+1] == ".":
            new_row += "^"
            continue
        if c+pvrow[pos+1] == "^^" and pvrow[pos-1] == ".":
            new_row += "^"
            continue
        if pvrow[pos-1] == "^" and c+pvrow[pos+1] == "..":
            new_row += "^"
            continue
        if pvrow[pos+1] == "^" and c+pvrow[pos-1] == "..":
            new_row += "^"
            continue
        new_row += '.'
    cnt += new_row.count(".")
    pvrow = "." + new_row + "."
print(cnt)
