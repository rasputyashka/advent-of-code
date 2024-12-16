import re
pattern = re.compile('.A.')
data = [x.strip() for x in open(0).readlines()]

cnt = 0
for r in range(len(data)):
    for c in range(len(data[r])):
        if pattern.match(data[r][c-1:c+2]):
            m_count = 0
            s_count = 0
            r_below = data[r+1:r+2]
            r_above = data[r-1:r]
            if r_below and r_above:
                r_below = r_below[0][c-1:c+2]
                r_above = r_above[0][c-1:c+2]
                
                if r_above[0] + data[r][c] + r_below[2] in ('SAM', 'MAS') and r_above[2] + data[r][c] + r_below[0] in ('SAM', 'MAS'):
                    cnt += 1
print(cnt)
