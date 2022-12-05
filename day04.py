from functions import comma_separated_ranges, timer


@timer
def load_data(file):
    return comma_separated_ranges(file)


@timer
def star_one(pairs):
    subsets = 0
    for pair in pairs:
        elf1, elf2 = set(range(pair[0][0], pair[0][1] + 1)
                         ), set(range(pair[1][0], pair[1][1] + 1))
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            subsets += 1
    return subsets


@timer
def star_two(pairs):
    overlaps = 0
    for pair in pairs:
        overlap = min(pair[0][1], pair[1][1]) - max(pair[0][0], pair[1][0])
        if overlap >= 0:
            overlaps += 1
    return overlaps


@timer
def main():
    # data = []
    data = load_data("day04input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
