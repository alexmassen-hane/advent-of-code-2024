import math
from typing import Tuple, List


def parse_input(input_path: str) -> Tuple[List[str], List[str]]:
    """
    The input file contains both rules and the lists to check.

    Example of the input file:

    47|53
    97|13
    97|61
    97|47

    75, 47, 61, 53, 29
    61, 12, 29
    97, 61, 53, 29, 13
    75, 29, 13
    """

    rules = []
    lists_to_check = []
    with open(input_path, "r") as file:
        for line in file.readlines():
            cleaned = line.rstrip()
            if len(cleaned) >= 1:
                if "|" in line:
                    # Get rules
                    rules.append(cleaned.split("|"))
                else:
                    # Get the lists
                    lists_to_check.append(cleaned.split(","))

    return rules, lists_to_check


def check_list(rules: List[str], to_check: List[str]) -> bool:
    """Check an incoming list to see if it works by the given rules or not."""

    for before, after in rules:
        try:
            before_index = to_check.index(before)
            if after in to_check[:before_index]:
                return False
        except:
            pass

    return True


rules, lists_to_check = parse_input("input.txt")

# Get the lists that are correct.
correct_lists = [line for line in lists_to_check if check_list(rules, line)]

count = 0
for line in correct_lists:
    # Find middle position and perform the sum.
    middle_pos = int(math.floor(float(len(line)) / 2.0))
    count += int(line[middle_pos])

print(f"Answer: {count}")
