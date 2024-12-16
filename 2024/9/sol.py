line = input()

position_mapping = []
current_sector = 0
max_compressed_size = 0
for pos, el in enumerate(line):
    if pos % 2 == 0:
        for i in range(int(el)):
            position_mapping.append(current_sector)
        max_compressed_size += int(el)
        current_sector += 1
    else:
        for i in range(int(el)):
            position_mapping.append('.')

idx = 0
while len(position_mapping) > max_compressed_size:
    if position_mapping[idx] == '.':
        if max_compressed_size == idx:
            for i in range(len(position_mapping[idx:])):
                position_mapping.pop()
            break
        last_val = position_mapping.pop()
        while last_val == '.':
            last_val = position_mapping.pop()
        position_mapping[idx] = last_val
    idx += 1

sm = 0


for pos, el in enumerate(position_mapping):
    sm += int(el) * pos

print(sm)
