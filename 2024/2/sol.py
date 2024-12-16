data = [[int(x) for x in y.split()] for y in open(0).readlines()]

cnt = 0

def check_layer(layer):
    if sorted(layer) == layer or sorted(layer, reverse=True) == layer:
        for a, b in zip(layer, layer[1:]):
            if a == b or abs(a - b) > 3:  # sorting still can not guarantee case where a, a in list
                return False
        else:
            return True # checks are passed
    return False  # non decreasing or incerasing

def get_fixed_layers(layer):
    options = [layer]
    for i in range(len(layer)):
        options.append(layer[:i] + layer[i+1:])
    return options

for line in data:
    for option in get_fixed_layers(line):
        if check_layer(option):
            cnt += 1
            break

print(cnt)
