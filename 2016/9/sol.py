import re

pattern = re.compile(r"\((\d+)x(\d+)\)")
string = open(0).read().strip()

def unpack(string):
    print(string)
    found = pattern.search(string)
    if not found:
        print("before end", len(string))
        return len(string)
    length = int(found.group(1))
    times = int(found.group(2))

    end = found.end()
    mul = unpack(string[end:end+length])
    res = len(string[:found.start()]) + mul * times + unpack(string[end+length:])
    print("after end", res)
    return res
print(unpack(string))
