import functools
from time import perf_counter
import functools

def comma_separated_line(filename):
    with open(filename, "r") as file_in:
        out = [x for x in file_in.read().strip("\n").split(", ")    ]
    return out


def timer(func):
    """courtesy of filakrad"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time} seconds.")
        return value
    return wrapper_timer


def lines(filename):
    with open(filename, "r") as file_in:
        out = [line for line in file_in.read().split("\n")]
    return out