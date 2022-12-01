from functions import blocks_of_lines, timer


@timer
def load_data(file):
    return blocks_of_lines(file)


@timer
def star_one(calories_list):
    most_cals = 0
    for elf in calories_list:
        cals = 0
        for cal in elf:
            cals += int(cal)
        most_cals = max(most_cals, cals)
    return most_cals


@timer
def star_two(calories_list):
    most_cals = []
    for elf in calories_list:
        cals = 0
        for cal in elf:
            cals += int(cal)
        most_cals.append(cals)
    return sum(sorted(most_cals, reverse=True)[0:3])


@timer
def main():
    data = load_data("day01input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
