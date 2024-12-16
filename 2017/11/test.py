s = input()
for i in range(100):
    s = s.replace("n,s,", "")
    s = s.replace("s,n,", "")
    s = s.replace("ne,nw,", "n,")
    s = s.replace("nw,ne,", "n,")
    s = s.replace("sw,se,", "s,")
    s = s.replace("se,sw,", "s,")
    s = s.replace("nw,se,", "")
    s = s.replace("se,nw,", "")
    s = s.replace("ne,sw,", "")
    s = s.replace("sw,ne,", "")

print(s)
