def main():
    with open('day03_input.txt') as file:
        wire1_steps = file.readline().strip().split(',')
        wire2_steps = file.readline().strip().split(',')

    wire1_visited = set()
    process_steps(wire1_steps, wire1_visited)

    wire2_visited = set()
    process_steps(wire2_steps, wire2_visited)

    intersections = wire1_visited & wire2_visited
    closest = min(intersections, key=lambda t: abs(t[0]) + abs(t[1]))
    print(f"The closest point is {closest} with manhattan distance {abs(closest[0]) + abs(closest[1])}")


def process_steps(steps, visited):
    curr = (0, 0)
    for step in steps:
        direction = step[0]
        n = int(step[1:])

        # construct a set with all the new visited positions
        if direction == 'U':
            new = [(curr[0], curr[1] + i) for i in range(1, n + 1)]
        elif direction == 'R':
            new = [(curr[0] + i, curr[1]) for i in range(1, n + 1)]
        elif direction == 'D':
            new = [(curr[0], curr[1] - i) for i in range(1, n + 1)]
        elif direction == 'L':
            new = [(curr[0] - i, curr[1]) for i in range(1, n + 1)]

        curr = new[-1]
        print(f"curr is now {curr}")
        visited.update(new)


if __name__ == '__main__':
    main()
