def main():
    with open('day05_input.txt') as file:
        contents = file.read()

    program = contents.strip().split(',')
    run_program(program, 5)


def run_program(program, input):
    curr_indx = 0

    while True:
        # Read the instruction at the instruction pointer
        instr = program[curr_indx].zfill(5)

        # Extract the opcode and parameter modes
        opcode = int(instr[-2:])
        modes = [int(x) for x in list(instr[2::-1])]

        # convenience function for interpreting parameter modes
        def get_arg_value(arg, mode):
            return int(program[arg]) if mode == 0 else arg

        if opcode in [1, 2, 7, 8]:
            # All three parameter ops that write a result to a given location
            args = [int(program[curr_indx + i]) for i in range(1, 4)]

            p1 = get_arg_value(args[0], modes[0])
            p2 = get_arg_value(args[1], modes[1])

            if opcode == 1:
                result = p1 + p2
            elif opcode == 2:
                result = p1 * p2
            elif opcode == 7:
                result = 1 if p1 < p2 else 0
            else:
                result = 1 if p1 == p2 else 0

            program[args[2]] = str(result)

            curr_indx += 4
        elif opcode in [5, 6]:
            # Two parameter jump ops that update the instruction pointer
            args = [int(program[curr_indx + i]) for i in range(1, 3)]

            p1 = get_arg_value(args[0], modes[0])
            p2 = get_arg_value(args[1], modes[1])

            if opcode == 5 and p1 != 0:
                curr_indx = p2
            elif opcode == 6 and p1 == 0:
                curr_indx = p2
            else:
                curr_indx += 3
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
