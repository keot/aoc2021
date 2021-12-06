#!/usr/bin/env python3

# Advent of Code 2021: Day 3


def read_file(filename="./demo"):
    with open(filename) as file_object:
        return [x.strip() for x in file_object.readlines()]


def _sum_columns(strings):
    results = [0] * len(strings[0])
    for index in range(len(strings[0])):
        results[index] = sum([int(x[index]) for x in strings])
    return results


def _binary_string_to_int(string):
    # Not sure what format AOC are using yet
    return int(string, 2)


def gamma_rate(strings):
    # Most common bits
    return "".join([str(int(c >= len(strings) / 2)) for c in _sum_columns(strings)])


def epsilon_rate(strings):
    # Most common bits
    return "".join([str(int(c < len(strings) / 2)) for c in _sum_columns(strings)])


def calculate_rating(strings, oxygen=True):
    for column in range(len(strings[0])):
        if oxygen:
            most_common = (
                "1" if sum(int(x[column]) for x in strings) >= len(strings) / 2 else "0"
            )
        else:
            most_common = (
                "0" if sum(int(x[column]) for x in strings) >= len(strings) / 2 else "1"
            )
        strings = [string for string in strings if string[column] == most_common]
        if len(strings) == 2:
            return sorted([_binary_string_to_int(x) for x in strings], reverse=oxygen)[
                0
            ]
        elif len(strings) == 1:
            return _binary_string_to_int(strings[0])

    return None


if __name__ == "__main__":
    # 1. What is the power consumption of the submarine?
    test_dataset = read_file("./demo")
    assert gamma_rate(test_dataset) == "10110"
    assert _binary_string_to_int("10110") == 22
    assert epsilon_rate(test_dataset) == "01001"
    assert _binary_string_to_int("01001") == 9

    dataset = read_file("./input")
    power_consumption = _binary_string_to_int(
        gamma_rate(dataset)
    ) * _binary_string_to_int(epsilon_rate(dataset))
    print(f"The submarine is consuming {power_consumption} power units.")

    # 2. Some strange calculation
    assert calculate_rating(test_dataset, oxygen=True) == 23
    assert calculate_rating(test_dataset, oxygen=False) == 10
    multiplied_ratings = calculate_rating(dataset, oxygen=True) * calculate_rating(
        dataset, oxygen=False
    )
    print(f"The submaine ratings multiplied are {multiplied_ratings}.")
