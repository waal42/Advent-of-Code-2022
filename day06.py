from functions import lines, timer


@timer
def load_data(file):
    return lines(file)[0]


@timer
def star_one(datastream):
    for i in range(len(datastream) - 4):
        marker = datastream[i:i+4]
        if len(marker) == len(set(marker)):
            break
    return i + 4


@timer
def star_two(datastream):
    for i in range(len(datastream) - 14):
        marker = datastream[i:i+14]
        if len(marker) == len(set(marker)):
            break
    return i + 14
    


@timer
def main():
    testdata = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
    data = load_data("day06input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
