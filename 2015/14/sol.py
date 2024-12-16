d = {}
results = []
SECONDS = 2503

for line in open(0).readlines():
    units = line.split()
    name = units[0]
    speed = int(units[3])
    fly_time = int(units[6])
    rest_time = int(units[-2])

    all_time = fly_time + rest_time
    if SECONDS % all_time < fly_time:
        time_left = SECONDS % all_time
    else:
        time_left = fly_time
    expr = SECONDS // all_time * speed * fly_time + speed * time_left
    results.append(expr)

print(max(results))
# actually you can a2dd 2503 // (fly_time and rest time) + 2053 % (fly_time + rest_time) > fly_time (or extended version if it is less than fly time).

