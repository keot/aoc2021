#!/usr/bin/env python3

# Advent of Code 2021: Day 1


def read_depths(filename="./demo"):
    with open(filename) as file_object:
        return [int(x) for x in file_object.readlines()]


def count_aggregate_depth(depths):
    return sum([x - y > 0 for x, y in zip(depths, [0] + depths)]) - 1


def windowed_values(values, window):
    return [sum(values[i : i + window]) for i in range(len(values) - window + 1)]


def count_aggregate_depth_windowed(depths, window):
    return count_aggregate_depth(windowed_values(depths, window))


if __name__ == "__main__":
    # 1. How many measurements are larger than the previous measurement?
    assert count_aggregate_depth(read_depths("./demo")) == 7
    descents = count_aggregate_depth(read_depths("./input"))
    print(f"We've descended {descents} measurements.")

    # 2. How many times does the sum of measurements in the sliding window of
    #    three increase?
    window = 3
    assert count_aggregate_depth_windowed(read_depths("./demo"), window) == 5
    descents = count_aggregate_depth_windowed(read_depths("./input"), window)
    print(f"We've descended {descents} measurements with a window of {window}.")
