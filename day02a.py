with open('day02_input.txt') as file:
    contents = file.read()

program = [int(x) for x in contents.split(',')]
for i in range(0, len(program), 4):
    opcode = program[i]
    if opcode == 99:
        break

    p1 = program[i + 1]
    p2 = program[i + 2]
    loc = program[i + 3]

    if opcode == 1:
        program[loc] = program[p1] + program[p2]
    elif opcode == 2:
        program[loc] = program[p1] * program[p2]

print(program)
