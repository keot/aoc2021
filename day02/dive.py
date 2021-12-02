#!/usr/bin/env python3

# Advent of Code 2021: Day 2


def read_course(filename="./demo"):
    # Reads in "forward 5" as a tuple
    with open(filename) as file_object:
        return [(x.split()[0], int(x.split()[1])) for x in file_object.readlines()]


def sum_aggregate(data):
    keys = set(x for x, _ in data)
    results = dict()
    for key in keys:
        results[key] = sum(y for x, y in data if x == key)
    return results


def question_one(data):
    aggs = sum_aggregate(data)
    horizontal = aggs["forward"]
    vertical = aggs["down"] - aggs["up"]
    return horizontal * vertical


def question_two(data):
    aim, horizontal, vertical = 0, 0, 0

    for operation, units in data:
        if operation == "down":
            aim += units
        elif operation == "up":
            aim -= units
        elif operation == "forward":
            horizontal += units
            vertical += aim * units
        else:
            raise ValueError(f"Operation {operation} unexpected!")

    return horizontal * vertical


if __name__ == "__main__":
    # 1. What do you get if you multiply your final horizontal position by your final depth?
    assert question_one(read_course("./demo")) == 150
    result = question_one(read_course("./input"))
    print(f"The result is {result}.")

    # 2. Horizontal multiplied by vertical for aim algorithm case:
    assert question_two(read_course("./demo")) == 900
    result = question_two(read_course("./input"))
    print(f"The result is {result}.")
