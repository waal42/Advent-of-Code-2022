from functions import tuples, timer
from pprint import pprint


@timer
def load_data(file):
    return tuples(file)


@timer
def star_one(instructions):
    register = 1
    cycle = 1
    signal_strengths = 0
    for instruction in instructions:
        if instruction[0] == "noop":
            cycle += 1
        elif instruction[0] == "addx":
            cycle += 1
            if cycle % 40 == 20:
                signal_strengths += cycle * register
            cycle += 1
            register += int(instruction[1])
        if cycle % 40 == 20:
            signal_strengths += cycle * register
    return signal_strengths


@timer
def star_two(instructions):
    register = 1
    display = list()
    line = list()
    instr = 0
    wait = False
    cycle = 1
    lines = 1
    while (cycle) * lines <= 240:
        if cycle in range(register, register + 3):
            line.append("#")
        else:
            line.append(" ")
        if instr in range(len(instructions)):
            print(cycle, register, instr, instructions[instr], wait, list(
                range(register - 1, register + 2)))
            print("".join(line))
            if instructions[instr][0] == "noop":
                instr += 1
            elif instructions[instr][0] == "addx":
                if wait:
                    register += int(instructions[instr][1])
                    wait = False
                    instr += 1
                else:
                    wait = True
        if (cycle) % 40 == 0 and cycle != 0:
            cycle -= 40
            lines += 1
            display.append(line)
            line = list()
        cycle += 1
    stringed_display = list()
    for disp in display:
        stringed_display.append("".join(disp))
    return stringed_display


@timer
def main():
    # data = []
    data = load_data("day10input.txt")
    print(star_one(data))
    pprint(star_two(data))


if __name__ == "__main__":
    main()
