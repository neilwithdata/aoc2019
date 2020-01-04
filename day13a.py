from collections import deque


class Program:
    def __init__(self, data):
        self.relative_base = 0
        self.curr_indx = 0
        self.inputs = deque()
        self.data = data[:]

    def queue_input(self, val):
        self.inputs.append(val)

    def p_val(self, indx, w_val=None):
        # Expand memory if necessary
        if indx >= len(self.data):
            self.data += ['0'] * (indx + 1 - len(self.data))

        if w_val:
            self.data[indx] = w_val

        return self.data[indx]

    def get_next_arg(self, mode, write=False):
        arg = int(self.p_val(self.curr_indx))
        self.curr_indx += 1

        if write:
            if mode == 0:
                return arg
            elif mode == 2:
                return self.relative_base + arg
        else:
            if mode == 0:  # position mode
                return int(self.p_val(arg))
            elif mode == 1:  # immediate mode
                return arg
            else:  # relative mode
                return int(self.p_val(self.relative_base + arg))

    def get_next_instruction(self):
        instr = self.p_val(self.curr_indx).zfill(5)

        opcode = int(instr[-2:])
        modes = [int(x) for x in list(instr[2::-1])]

        self.curr_indx += 1
        return opcode, modes

    def run(self):
        while True:
            opcode, modes = self.get_next_instruction()

            if opcode in [1, 2, 7, 8]:
                # All three parameter ops that write a result to a given location
                p1 = self.get_next_arg(modes[0])
                p2 = self.get_next_arg(modes[1])

                if opcode == 1:
                    result = p1 + p2
                elif opcode == 2:
                    result = p1 * p2
                elif opcode == 7:
                    result = 1 if p1 < p2 else 0
                else:
                    result = 1 if p1 == p2 else 0

                dest = self.get_next_arg(modes[2], write=True)

                self.p_val(dest, str(result))
            elif opcode in [5, 6]:
                # Two parameter jump ops that update the instruction pointer
                p1 = self.get_next_arg(modes[0])
                p2 = self.get_next_arg(modes[1])

                if (opcode == 5 and p1 != 0) or (opcode == 6 and p1 == 0):
                    self.curr_indx = p2
            elif opcode == 3:  # Input
                dest = self.get_next_arg(modes[0], write=True)
                self.p_val(dest, self.inputs.popleft())
            elif opcode == 4:  # Output
                output = self.get_next_arg(modes[0])
                yield str(output)
            elif opcode == 9:  # Change relative base
                offset = self.get_next_arg(modes[0])
                self.relative_base += offset
            elif opcode == 99:  # Exit
                return


def main():
    with open('day13_input.txt') as file:
        contents = file.read()

    program = Program(contents.strip().split(','))
    it = iter(program.run())

    screen = {}
    while True:
        try:
            x, y, tile_id = int(next(it)), int(next(it)), int(next(it))
            screen[(x, y)] = tile_id
        except StopIteration:
            break  # we're done

    print(f'Num block tiles: {list(screen.values()).count(2)}')


if __name__ == '__main__':
    main()
