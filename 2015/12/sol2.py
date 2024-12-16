# [1,{"c":"red","b":2},3]

data = eval(input())

def dfs(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return 0
    if isinstance(obj, list):
        sm = 0
        for o in obj:
            sm += dfs(o)
        return sm
    elif isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        else:
            sm = 0
            for o in obj.values():
                sm += dfs(o)
    return sm

print(dfs(data))

