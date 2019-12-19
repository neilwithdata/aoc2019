from collections import namedtuple
from math import sqrt, atan2

Point = namedtuple('Point', 'x y')


def distance(a, b):
    return sqrt((b.y - a.y) ** 2 + (b.x - a.x) ** 2)


def angle(a, b):
    return atan2(b.y - a.y, b.x - a.x)


positions = []
with open('day10_input.txt') as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            if c == '#':
                positions.append(Point(x, y))

# print('starting positions', positions)

max_count = 0
for pos_a in positions:
    obscured = set()

    for pos_b in positions:
        if pos_a == pos_b or pos_b in obscured:
            continue

        ab_dist = distance(pos_a, pos_b)
        ab_angle = angle(pos_a, pos_b)
        # print(f'distance {ab_dist} and angle {ab_angle} between {pos_a} and {pos_b}')

        # Find any other points with the same angle but greater distance (obscured)
        for pos_c in positions:
            if pos_c == pos_a or pos_c == pos_b or pos_c in obscured:
                continue

            ac_angle = angle(pos_a, pos_c)
            ac_dist = distance(pos_a, pos_c)

            if ac_angle == ab_angle and ac_dist > ab_dist:
                obscured.add(pos_c)

    max_count = max(max_count, len(positions) - len(obscured) - 1)
    # print(f'\n\nFrom position {pos_a} the following positions are obscured: {obscured}\n\n')

print('best location detectable count:', max_count)
