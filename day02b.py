import sys

with open('day02_input.txt') as file:
    contents = file.read()

init_program = [int(x) for x in contents.split(',')]


def run_program(noun, verb, program):
    program[1] = noun
    program[2] = verb

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

    return program[0]


for i in range(100):
    for j in range(100):
        output = run_program(i, j, init_program[:])
        if output == 19690720:
            print(100 * i + j)
            sys.exit()
