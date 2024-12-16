data = [x.strip() for x in open(0).readlines()]

cnt = 0
start = 0 + 0j

for x in data:
    cnt += x.count('XMAS')
    cnt += x.count('SAMX')

for r in range(len(data)):
    for c in range(len(data[r])):
        res = []
        word = ''
        for t in range(r, r+4):
            row = data[t:t+1]
            if row:
                word += row[0][c:c+1]  # not to deal with IndexError, data[t:t+1] returns list with possibly empty string
        if word == 'XMAS' or word == 'SAMX':
            cnt += 1

for r in range(len(data)):
    for c in range(len(data[r])):
        word_r = ''
        word_l = ''
        res_r = []
        res_l = []

        for t in range(4):
            row = data[r+t:r+t+1]
            if row:
                char = row[0][c+t:c+t+1]
                word_r += char
                res_r.append((r+t+1, c+t+1, char))
        for t in range(4):
            row = data[r+t:r+t+1]
            if row:
                char = row[0][c-t:c-t+1]
                word_l += char
                res_l.append((r+t+1, c-t+1, char))
        
        if word_r in ('SAMX', 'XMAS'):
            #print(res_r, 'R')
            cnt += 1
        if word_l in ('SAMX', 'XMAS'):
            #print(res_l, 'L')
            cnt += 1

print(cnt)
