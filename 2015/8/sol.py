unformatted = 0
formatted = 0
t = 0

for line in open(0, mode="r"):
    line = line.strip()
    formatted += len(eval(line))
    unformatted += len(line)
    print(formatted, unformatted)

print(unformatted - formatted)
