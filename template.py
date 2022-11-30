from functions import lines, timer

@timer
def load_data(file):
    return lines(file)


@timer
def star_one(data_in):
    pass


@timer
def star_two(data_in):
    pass


@timer
def main():
    # data = []
    data = load_data("day00input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
