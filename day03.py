from functions import lines, timer


@timer
def load_data(file):
    return lines(file)


def count_priority(char):
    if ord(char) in range(65, 91):
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96


@timer
def star_one(rucksacks):
    errors = list()
    for rucksack in rucksacks:
        half = int(len(rucksack)/2)
        first_compartment = rucksack[0:half]
        for item in rucksack[half:]:
            if item in first_compartment:
                errors.append(count_priority(item))
                break
    return sum(errors)


@timer
def star_two(rucksacks):
    badges = list()
    groups = list(zip(*(iter(rucksacks),) * 3))
    for group in groups:
        candidates = list()
        for letter in group[1]:
            if letter in group[0]:
                candidates.append(letter)
        for candidate in candidates:
            if candidate in group[2]:
                badges.append(count_priority(candidate))
                break
    return sum(badges)

@timer
def main():
    # data = []
    data = load_data("day03input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
