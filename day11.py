from functions import blocks_of_lines, timer
from math import floor, prod
from copy import deepcopy


@timer
def load_data(file):
    raw_monkeys = blocks_of_lines(file)
    monkeys = dict()
    for monkey in raw_monkeys:
        index = int(monkey[0].split()[1].strip(":"))
        items = [int(item) for item in monkey[1].split(":")[1].split(",")]
        operation = monkey[2].split("=")[1].lstrip()
        test = int(monkey[3].split()[3])
        test_true = int(monkey[4].split()[5])
        test_false = int(monkey[5].split()[5])
        monkeys[index] = {
            "items": items,
            "operation": operation,
            "test": test,
            "test_true": test_true,
            "test_false": test_false,
            "inspects": 0
        }
    return monkeys


@timer
def star_one(monkeys):
    for _ in range(20):
        for monkey in monkeys.keys():
            for item in monkeys[monkey]["items"]:
                new_item = eval(
                    monkeys[monkey]["operation"].replace("old", str(item)))
                divided = floor(new_item / 3)
                t_true = monkeys[monkey]["test_true"]
                t_false = monkeys[monkey]["test_false"]
                if divided % monkeys[monkey]["test"] == 0:
                    monkeys[t_true]["items"].append(divided)
                else:
                    monkeys[t_false]["items"].append(divided)
                monkeys[monkey]["inspects"] += 1
            monkeys[monkey]["items"] = list()
    inspects = list()
    for monkey in monkeys:
        inspects.append(monkeys[monkey]["inspects"])
    return prod(sorted(inspects, reverse=True)[:2])


@timer
def star_two(monkeys):
    lcm = 1
    for monkey in monkeys.keys():
        lcm *= monkeys[monkey]["test"]
    print(lcm)
    for _ in range(10000):
        for monkey in monkeys.keys():
            for item in monkeys[monkey]["items"]:
                new_item = eval(
                    monkeys[monkey]["operation"].replace("old", str(item % lcm)))
                t_true = monkeys[monkey]["test_true"]
                t_false = monkeys[monkey]["test_false"]
                if new_item % monkeys[monkey]["test"] == 0:
                    monkeys[t_true]["items"].append(new_item)
                else:
                    monkeys[t_false]["items"].append(new_item)
                monkeys[monkey]["inspects"] += 1
            monkeys[monkey]["items"] = list()
    inspects = list()
    for monkey in monkeys:
        inspects.append(monkeys[monkey]["inspects"])
    return prod(sorted(inspects, reverse=True)[:2])


@timer
def main():
    # data = []
    data = load_data("day11input.txt")
    print(star_one(deepcopy(data)))
    print(star_two(deepcopy(data)))


if __name__ == "__main__":
    main()
