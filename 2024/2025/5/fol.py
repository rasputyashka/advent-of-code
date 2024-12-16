
from collections import defaultdict
from pprint import pprint as print
from copy import deepcopy

check_data_processing = False
dct = defaultdict(dict)
updates = []

for line in open(0).readlines():
    line = line.strip()
    if not line:
        check_data_processing = True
        continue
    if not check_data_processing:
        prev, after = line.split('|')

        dct[after]['prev'] = dct[after].get('prev') or set()

        dct[after]['prev'].add(prev)

    else:
        updates.append(line.split(','))

sm = 0

new_dct = {}
for _ in range(100):
    for key, value in dct.items():
        new_dct[key] = value
        if 'prev' in value:
            for prev_val in value['prev']:
                print(value['prev'])
                print(dct[prev_val]['prev'])
                try:
                    new_dct[key]['prev'] |= dct[prev_val]['prev']
                except KeyError:
                    pass
    dct = new_dct

print(new_dct)

