from sys import maxsize

def main():
    with open('day03_input.txt') as file:
        wire1_steps = file.readline().strip().split(',')
        wire2_steps = file.readline().strip().split(',')

    wire1_visited = process_steps(wire1_steps)
    wire2_visited = process_steps(wire2_steps)

    intersections = set(wire1_visited) & set(wire2_visited)

    min_steps = maxsize
    for intersection in intersections:
        steps = wire1_visited.index(intersection) + wire2_visited.index(intersection) + 2
        if steps < min_steps:
            min_steps = steps

    print(min_steps)


def process_steps(steps):
    curr = (0, 0)
    visited = []

    for step in steps:
        direction = step[0]
        n = int(step[1:])

        if direction == 'U':
            new = [(curr[0], curr[1] + i) for i in range(1, n + 1)]
        elif direction == 'R':
            new = [(curr[0] + i, curr[1]) for i in range(1, n + 1)]
        elif direction == 'D':
            new = [(curr[0], curr[1] - i) for i in range(1, n + 1)]
        elif direction == 'L':
            new = [(curr[0] - i, curr[1]) for i in range(1, n + 1)]

        curr = new[-1]
        visited += new

    return visited


if __name__ == '__main__':
    main()
