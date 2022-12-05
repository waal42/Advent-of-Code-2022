from functions import timer, blocks_of_lines
from copy import deepcopy


@timer
def load_data(file):
    instructions = blocks_of_lines(file)[1]
    short_instr = list()
    for instruction in instructions:
        num_instr = instruction.split(" from ")
        boxes = int(num_instr[0].lstrip("move "))
        from_to = list(map(int, num_instr[1].split(" to ")))
        short_instr.append((boxes, from_to))
    return short_instr


@timer
def star_one(init_stack, instructions):
    stack = deepcopy(init_stack)
    for instr in instructions:
        boxes = instr[0]
        mv_from, mv_to = instr[1]
        while (boxes):
            stack[mv_to].append(stack[mv_from][len(stack[mv_from]) - 1])
            stack[mv_from] = stack[mv_from][:len(stack[mv_from]) - 1]
            boxes -= 1
    top_boxes = list()
    for line in stack:
        top_boxes.append(stack[line][-1])
    return "".join(top_boxes)


@timer
def star_two(init_stack, instructions):
    stack = deepcopy(init_stack)
    for instr in instructions:
        boxes = instr[0]
        mv_from, mv_to = instr[1]
        stack[mv_to] = stack[mv_to] + stack[mv_from][-boxes:]
        stack[mv_from] = stack[mv_from][:-boxes]
    top_boxes = list()
    for line in stack:
        if stack[line]:
            top_boxes.append(stack[line][-1])
    return "".join(top_boxes)


@timer
def main():
    instructions = load_data("day05input.txt")
    test_stack = {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"]
    }
    stack = {
        1: list("RNFVLJSM"),
        2: list("PNDZFJWH"),
        3: list("WRCDG"),
        4: list("NBS"),
        5: list("MZWPCBFN"),
        6: list("PRMW"),
        7: list("RTNGLSW"),
        8: list("QTHFNBV"),
        9: list("LMHZNF")
    }
    print(star_one(stack, instructions))
    print(star_two(stack, instructions))


if __name__ == "__main__":
    main()
