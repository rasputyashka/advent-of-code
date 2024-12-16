line = input()
for _ in range(50):
    new_string = ""
    cnt = 0
    cur_digit = line[0]
    for c in line:
        if c == cur_digit:
            cnt += 1
        else:
            new_string += str(cnt) + cur_digit
            cnt = 1
            cur_digit = c
    new_string += str(cnt) + cur_digit
    line = new_string
    print(line, len(line))
