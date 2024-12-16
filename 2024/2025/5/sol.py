from collections import defaultdict
from pprint import pprint as print

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

        dct[prev]['after'] = dct[prev].get('after') or []
        dct[after]['prev'] = dct[after].get('prev') or []

        dct[prev]['after'].append(after)
        dct[after]['prev'].append(prev)

    else:
        updates.append(line.split(','))

sm = 0

for update in updates:
    expired = set()
    correct = True
    for page in update:
        if page in expired:
            correct = False
            break
        try:
            prev_pages = dct[page]['prev']
            expired = expired.union(prev_pages, [page])
        except KeyError: # number was not in ruleset, It has no restrictions
            pass
    
    if correct:
        sm += int(update[len(update)//2])

print(sm)
