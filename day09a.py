def main():
    with open('day09_input.txt') as file:
        contents = file.read()

    program = contents.strip().split(',')
    run_program(program, '1')


def run_program(program, input):
    relative_base = 0
    curr_indx = 0

    def get_instruction():
        nonlocal curr_indx

        instr = p_val(curr_indx).zfill(5)

        opcode = int(instr[-2:])
        modes = [int(x) for x in list(instr[2::-1])]

        curr_indx += 1
        return opcode, modes

    def p_val(indx, w_val=None):
        nonlocal program

        # Expand memory if necessary
        if indx >= len(program):
            program += ['0'] * (indx + 1 - len(program))

        if w_val:
            program[indx] = w_val

        return program[indx]

    def get_next_arg(mode, write=False):
        nonlocal curr_indx

        arg = int(p_val(curr_indx))
        curr_indx += 1

        if write:
            if mode == 0:
                return arg
            elif mode == 2:
                return relative_base + arg
        else:
            if mode == 0:  # position mode
                return int(p_val(arg))
            elif mode == 1:  # immediate mode
                return arg
            else:  # relative mode
                return int(p_val(relative_base + arg))

    while True:
        opcode, modes = get_instruction()

        if opcode in [1, 2, 7, 8]:
            # All three parameter ops that write a result to a given location
            p1 = get_next_arg(modes[0])
            p2 = get_next_arg(modes[1])

            if opcode == 1:
                result = p1 + p2
            elif opcode == 2:
                result = p1 * p2
            elif opcode == 7:
                result = 1 if p1 < p2 else 0
            else:
                result = 1 if p1 == p2 else 0

            dest = get_next_arg(modes[2], write=True)

            p_val(dest, str(result))
        elif opcode in [5, 6]:
            # Two parameter jump ops that update the instruction pointer
            p1 = get_next_arg(modes[0])
            p2 = get_next_arg(modes[1])

            if (opcode == 5 and p1 != 0) or (opcode == 6 and p1 == 0):
                curr_indx = p2
        elif opcode == 3:  # Input
            dest = get_next_arg(modes[0], write=True)
            p_val(dest, input)
        elif opcode == 4:  # Output
            output = get_next_arg(modes[0])
            print(f'{output=}')
        elif opcode == 9:  # Change relative base
            offset = get_next_arg(modes[0])
            relative_base += offset
        elif opcode == 99:  # Exit
            return


if __name__ == '__main__':
    main()
