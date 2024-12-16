from collections import defaultdict
paths = defaultdict(dict)

cities = set()
for line in open(0).readlines():
    from_, _, to, _, value = line.split()
    value = int(value)
    paths[from_][to] = value
    paths[to][from_] = value
    cities.add(from_)
    cities.add(to)

cnt = len(cities)

from pprint import pprint
# pprint(paths)

# defaultdict(<class 'dict'>,
  #          {'Belfast': {'Dublin': 141, 'London': 518},
   #          'Dublin': {'Belfast': 141, 'London': 464},
    #         'London': {'Belfast': 518, 'Dublin': 464}})
def dfs(city, dst, visited):
    visited = visited.copy()
    visited.add(city)
    if len(visited) == cnt:
        return dst
    results = []
    for ncity in paths[city]:
        if ncity not in visited:
            res = dfs(ncity, dst+paths[city][ncity], visited)
            results.append(res)
 #   print(results)
    return max(results)

ans = 0
for city in paths:
    ans = max(ans, dfs(city, 0, set()))
print(ans)

