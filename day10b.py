from dataclasses import dataclass
from math import sqrt, atan2, degrees


@dataclass
class Point:
    x: int
    y: int
    angle: float = 0.0
    distance: float = 0.0


def distance(a, b):
    return sqrt((b.y - a.y) ** 2 + (b.x - a.x) ** 2)


def flatten_angle(a, b):
    deg = degrees(atan2(b.y - a.y, b.x - a.x))

    deg += 90
    if deg < 0:
        deg = 360 + deg
    return deg


STATION = Point(19, 14)

positions = []
with open('day10_input.txt') as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            if x == STATION.x and y == STATION.y:
                continue

            if c == '#':
                p = Point(x, y)
                p.angle = flatten_angle(STATION, p)
                p.distance = distance(STATION, p)
                positions.append(p)

# sort by angle, then by distance (from main station)
positions.sort(key=lambda pos: (pos.angle, pos.distance))

# walk through list in order, finding next largest angle and deleting as found
indx = 0
angle = -1
del_count = 0
while True:
    curr = positions[indx]
    if curr.angle > angle:
        del_count += 1
        angle = curr.angle

        print(f'The {del_count}th to be deleted is {curr.x, curr.y}')
        del positions[indx]

        if del_count == 200:
            break
    else:
        indx += 1
