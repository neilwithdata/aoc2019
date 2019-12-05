LOWER_BOUND = 245182
UPPER_BOUND = 790572

matches = 0
for n in range(LOWER_BOUND, UPPER_BOUND):
    str_n = str(n)

    adj = False
    prev = int(str_n[0])
    for digit in str_n[1:]:
        curr = int(digit)
        if curr < prev:
            break
        elif curr == prev:
            adj = True

        prev = curr
    else:
        if adj:
            matches += 1

print(matches)
