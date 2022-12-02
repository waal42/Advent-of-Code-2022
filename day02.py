from functions import tuples, timer


@timer
def load_data(file):
    return tuples(file)


@timer
def star_one(matches):
    wins = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    draws = [["A", "X"], ["B", "Y"], ["C", "Z"]]
    scoring = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for match in matches:
        if match in wins:
            score += 6
        elif match in draws:
            score += 3
        score += scoring[match[1]]
    return score


@timer
def star_two(matches):
    score = 0
    shapes = ["A", "B", "C"]
    match_scores = {"X": 0, "Y": 3, "Z": 6}
    for [shape, ending] in matches:
        score += match_scores[ending]
        if ending == "Z":
            score += (shapes.index(shape) + 1) % 3 + 1
        elif ending == "Y":
            score += shapes.index(shape) % 3 + 1
        else:
            score += (shapes.index(shape) - 1) % 3 + 1
    return score


@timer
def main():
    # data = []
    data = load_data("day02input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
