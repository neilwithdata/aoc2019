def main():
    with open('day05_input.txt') as file:
        contents = file.read()

    program = contents.strip().split(',')
    run_program(program, 1)


def run_program(program, input):
    curr_indx = 0

    while True:
        # Read the instruction at the instruction pointer
        instr = program[curr_indx].zfill(5)

        # Two rightmost digits indicate the opcode
        opcode = int(instr[-2:])

        def get_arg_value(arg, mode):
            return int(program[arg]) if mode == 0 else arg

        if opcode == 1 or opcode == 2:  # Addition/Multiplication
            args = [int(program[curr_indx + i]) for i in range(1, 4)]
            modes = [int(x) for x in list(instr[2::-1])]

            p1 = get_arg_value(args[0], modes[0])
            p2 = get_arg_value(args[1], modes[1])

            result = p1 + p2 if opcode == 1 else p1 * p2
            program[args[2]] = str(result)

            curr_indx += 4
        elif opcode == 3:  # Input
            dest = int(program[curr_indx + 1])
            program[dest] = str(input)
            curr_indx += 2
        elif opcode == 4:  # Output
            source = int(program[curr_indx + 1])
            print(f'Output: {program[source]}')
            curr_indx += 2
        elif opcode == 99:  # Exit
            break


if __name__ == '__main__':
    main()
