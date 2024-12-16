d = {}

for line in open(0).readlines():
    units = line.split()
    name = units[0]
    speed = int(units[3])
    fly_time = int(units[6])
    rest_time = int(units[-2])

    all_time = fly_time + rest_time
    d[name] = {}
    d[name]["fly_time"] = fly_time
    d[name]["all_time"] = all_time
    d[name]["speed"] = speed
    d[name]["score"] = 0

for sec in range(1, 2503):
    results = []
    for racer in d:
        fly_time = d[racer]["fly_time"]
        all_time = d[racer]["all_time"]
        speed = d[racer]["speed"]
        time_left = fly_time
        if sec % all_time < fly_time:
            time_left = sec % all_time
        cur_dist = sec // all_time * speed * fly_time + speed * time_left
        results.append((cur_dist, racer))
    maxval = max(results)[0]
    for x in results:
        if x[0] == maxval:
            d[x[1]]["score"] += 1

    print(max(results)[1])
print(max([d[x]["score"] for x in d]))
