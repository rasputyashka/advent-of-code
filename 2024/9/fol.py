from collections import Counter

line = input()

position_mapping = []
current_sector = 0
blanks = {}

for pos, el in enumerate(line):
    if pos % 2 == 0:
        for i in range(int(el)):
            position_mapping.append(current_sector)
        current_sector += 1
    else:
        for i in range(int(el)):
            position_mapping.append('.')

counter = Counter(position_mapping)
for i in range(len(position_mapping)-1):
    cnt = int(position_mapping[i] == '.')
    j = i

    while position_mapping[j] == position_mapping[j+1] == '.':
        j += 1
        cnt += 1

    if cnt >= 1:
        blanks[cnt] = blanks.get(cnt) or []
        blanks[cnt].append((i, j+1))  # for slicing

for v in sorted(counter.keys() - set('.'), reverse=True):
    print(v)

