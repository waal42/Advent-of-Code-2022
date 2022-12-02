import functools
from time import perf_counter


def timer(func):
    """- courtesy of filakrad"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time} seconds.")
        return value
    return wrapper_timer


def comma_separated_line(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return list(file_in.read().strip("\n").split(", "))


def lines(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return list(file_in.read().split("\n"))


def blocks_of_lines(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return [line.split("\n") for line in file_in.read().split("\n\n")]


def tuples(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return [tuple.split(" ") for tuple in file_in.read().split("\n")]
