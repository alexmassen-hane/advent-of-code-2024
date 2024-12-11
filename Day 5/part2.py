import math


def parse_input(input_path):
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


def check_list(rules, to_check) -> bool:
    """Check an incoming list to see if it works by the given rules or not."""

    for before, after in rules:
        try:
            before_index = to_check.index(before)
            if after in to_check[:before_index]:
                after_index = to_check.index(after)
                return False, before_index, after_index
        except:
            pass

    # If it is not found in the list, it is correct.
    return True, None, None


def make_list_correct(rules, to_change):
    """Make a list correct by using the rules to switch the before and after parts until it is correct."""

    list_is_correct, before_index, after_index = check_list(rules, to_change)
    if list_is_correct:
        # Return nothing if the list is already correct.
        return None

    while not list_is_correct:

        temp = to_change[after_index]
        to_change[after_index] = to_change[before_index]
        to_change[before_index] = temp

        list_is_correct, before_index, after_index = check_list(rules, to_change)

    # Return the corrected list
    return to_change


rules, lists_to_check = parse_input("input.txt")

# Get the lists that are incorrect and make them correct.
correct_lists = [
    corrected
    for line in lists_to_check
    if (corrected := make_list_correct(rules, line))
]

count = 0
for line in correct_lists:
    # Find middle position and perform the sum.
    middle_pos = int(math.floor(float(len(line)) / 2.0))
    count += int(line[middle_pos])

print(f"Answer: {count}")
