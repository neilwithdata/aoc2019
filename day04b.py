LOWER_BOUND = 245182
UPPER_BOUND = 790572

match_count = 0
for n in range(LOWER_BOUND, UPPER_BOUND):
    str_n = str(n)

    prev = (int(str_n[0]), 1)
    match = False
    for digit in str_n[1:]:
        curr = int(digit)
        if curr < prev[0]:
            match = False
            break
        elif curr == prev[0]:
            prev = (prev[0], prev[1] + 1)
        else:
            if prev[1] == 2:
                match = True

            prev = (curr, 1)
    else:
        if prev[1] == 2:
            match = True

    if match:
        match_count += 1

print(match_count)
