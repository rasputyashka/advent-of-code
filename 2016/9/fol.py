
cnt = 0
line = input()
cur_word = ""
idx = 0
while idx < len(line):
    if line[idx] == "(":
        distance = line[idx:].find(")") + idx
        bracket_end = distance
        length, times = get_comp_data(line[idx+1:bracket_end])
        idx = bracket_end + 1
        to_repeat = line[idx: idx + length]
        cur_word += to_repeat * times
        idx += length
    else:
        cur_word += line[idx]
        idx += 1
cnt += len(cur_word) - cur_word.count(" ")
print(cnt)
