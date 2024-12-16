from collections import defaultdict
from concurrent import futures

rps = defaultdict(list)
ready = False

START = "e"

for line in open(0).readlines():
    line = line.strip()
    if ready:
        string = line
    if not ready:
        if line == '':
            ready = True
            continue
        from_, _, to = line.split()
        rps[from_].append(to)

def foo(string):
    got = set()
    for f, tos in rps.items():
        for to in tos: # h ho
            idx = 0 # 
            while f in string[idx:]: # 1 - hoh 2 - oh
                idx = max(string[idx:].find(f), idx) # 0 - # 1
                tail = string[:idx] # "" # h
                head = string[idx:] # hoh # oh
                got.add(tail+head.replace(f, to, 1)) # ho
                idx += 1
    return got
executor = futures.ProcessPoolExecutor()
res = {"e", }
cnt = 0
while string not in res:
    cnt += 1
    local_res = set()
    for new_res in executor.map(foo, res):
        local_res |= new_res
    res = local_res
print(cnt)
