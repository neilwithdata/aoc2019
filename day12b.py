import itertools
import math
import re


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# pos/vel here are [x0, x1, x2, x3]
def cycle_length(pos, vel):
    init_pos = pos[:]
    init_vel = vel[:]

    pairs = list(itertools.combinations(range(4), 2))

    step_count = 0
    while True:
        # first apply gravity between each pair of positions
        for m1, m2 in pairs:
            if pos[m1] > pos[m2]:
                vel[m1] -= 1
                vel[m2] += 1
            elif pos[m1] < pos[m2]:
                vel[m1] += 1
                vel[m2] -= 1

        # next update the positions based on the velocities
        pos = [p + q for p, q in zip(pos, vel)]

        step_count += 1
        if pos == init_pos and vel == init_vel:
            return step_count


moons = []
with open('day12_input.txt') as file:
    for line in file:
        moons.append([int(n) for n in re.findall(r'-?\d+', line)])

x_cycle = cycle_length([moons[n][0] for n in range(4)], [0, 0, 0, 0])
y_cycle = cycle_length([moons[n][1] for n in range(4)], [0, 0, 0, 0])
z_cycle = cycle_length([moons[n][2] for n in range(4)], [0, 0, 0, 0])

print(lcm(x_cycle, lcm(y_cycle, z_cycle)))
