from functions import tuples, timer
from pprint import pprint


@timer
def load_data(file):
    return tuples(file)


@timer
def star_one(motions):
    h_x, h_y = 0, 0
    t_x, t_y = 0, 0
    tail_positions = [(t_x, t_y)]
    for motion in motions:
        [dir, dist] = [motion[0], int(motion[1])]
        if dir == "L":
            vector = [-1, 0]
        elif dir == "R":
            vector = [1, 0]
        elif dir == "U":
            vector = [0, 1]
        else:
            vector = [0, -1]
        for _ in range(dist):
            h_x += vector[0]
            h_y += vector[1]
            if abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1:
                if h_x == t_x:
                    if h_y > t_y:
                        t_y += 1
                    else:
                        t_y -= 1
                elif h_y == t_y:
                    if h_x > t_x:
                        t_x += 1
                    else:
                        t_x -= 1
                else:
                    if h_x > t_x:
                        t_x += 1
                        if h_y > t_y:
                            t_y += 1
                        else:
                            t_y -= 1
                    else:
                        t_x -= 1
                        if h_y > t_y:
                            t_y += 1
                        else:
                            t_y -= 1
                tail_positions.append((t_x, t_y))
    return len(set(tail_positions))


@timer
def star_two(motions):
    knots = dict()
    tail_positions = [(0, 0)]
    for knot in range(10):
        knots[knot] = [0, 0]
    for motion in motions:
        [dir, dist] = [motion[0], int(motion[1])]
        if dir == "L":
            vector = [-1, 0]
        elif dir == "R":
            vector = [1, 0]
        elif dir == "U":
            vector = [0, 1]
        else:
            vector = [0, -1]
        for _ in range(dist):
            knots[0][0] += vector[0]
            knots[0][1] += vector[1]
            for knot in knots.keys():
                if knot == 0:
                    continue
                if abs(knots[knot-1][0] - knots[knot][0]) > 1 or abs(knots[knot-1][1] - knots[knot][1]) > 1:
                    if knots[knot-1][0] == knots[knot][0]:
                        if knots[knot-1][1] > knots[knot][1]:
                            knots[knot][1] += 1
                        else:
                            knots[knot][1] -= 1
                    elif knots[knot-1][1] == knots[knot][1]:
                        if knots[knot-1][0] > knots[knot][0]:
                            knots[knot][0] += 1
                        else:
                            knots[knot][0] -= 1
                    else:
                        if knots[knot-1][0] > knots[knot][0]:
                            knots[knot][0] += 1
                            if knots[knot-1][1] > knots[knot][1]:
                                knots[knot][1] += 1
                            else:
                                knots[knot][1] -= 1
                        else:
                            knots[knot][0] -= 1
                            if knots[knot-1][1] > knots[knot][1]:
                                knots[knot][1] += 1
                            else:
                                knots[knot][1] -= 1
            tail_positions.append(tuple(knots[9]))
    return len(set(tail_positions))
    


@timer
def main():
    # data = []
    data = load_data("day09input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
