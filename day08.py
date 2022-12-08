from functions import lines, timer


@timer
def load_data(file):
    return lines(file)


@timer
def star_one(forest):
    visible_trees = 4 * (len(forest) - 1)
    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest[0]) - 1):
            if forest[y][x] > max(forest[y][:x]):
                visible_trees += 1
                continue
            if forest[y][x] > max(forest[y][x+1:]):
                visible_trees += 1
                continue
            up = [forest[y_up][x] for y_up in range(0, y)]
            if forest[y][x] > max(up):
                visible_trees += 1
                continue
            down = [forest[y_down][x] for y_down in range(y+1, len(forest))]
            if forest[y][x] > max(down):
                visible_trees += 1
                continue
    return visible_trees


@timer
def star_two(forest):
    scenic_score = 0
    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest[0]) - 1):
            left = 0
            right = 0
            up = 0
            down = 0
            for x_left in range(x-1, -1, -1):
                left += 1
                if forest[y][x] <= forest[y][x_left]:
                    break
            for x_right in range(x+1, len(forest[0]), 1):
                right += 1
                if forest[y][x] <= forest[y][x_right]:
                    break
            for y_up in range(y-1, -1, -1):
                up += 1
                if forest[y][x] <= forest[y_up][x]:
                    break
            for y_down in range(y+1, len(forest), 1):
                down += 1
                if forest[y][x] <= forest[y_down][x]:
                    break
            scenic_score = max(scenic_score, left*right*up*down)
    return scenic_score


@timer
def main():
    # data = []
    data = load_data("day08input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
