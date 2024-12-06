def get_sign(number):
    return (number > 0) - (number < 0)


def check_safe(levels):
    last_sign = get_sign(levels[1] - levels[0])
    for i in range(1, len(levels), 1):
        diff = levels[i] - levels[i - 1]
        new_sign = get_sign(diff)

        # Check if all increasing or decreasing
        if last_sign != new_sign:
            print(
                f"Sign change: last sign and new sign different! i={i} diff={diff} last_sign={last_sign} new_sign={new_sign}"
            )
            return False, i

        # Check if the differences are within bounds
        if abs(diff) < 1 or abs(diff) > 3:
            print(f"diff not within bounds: i={i} {diff}")
            return False, i

        last_sign = new_sign

    print(f"Good! - {levels}")
    return True, i


with open("input.txt", "r") as file:
    raw_data = file.readlines()

data = []
for line in raw_data:
    cleaned = line.rstrip().split(" ")
    data.append([int(x) for x in cleaned])

# test
data = [
    [3, 2, 3, 4, 5],
    [1, 2, 3, 4, 4],
    [8, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [37, 38, 37, 34, 31],
    [75, 77, 72, 70, 69],
]

num_safe = 0
for levels in data:

    print(f"--- New levels ---")
    print(levels)
    rev_levels = levels[::-1]

    check, bad_loc = check_safe(levels)
    rev_check, rev_bad_loc = check_safe(rev_levels)
    if check or rev_check:
        num_safe += 1
    else:
        # Try again by removing the bad reading

        # I very much cheese this one. Instead of improving my logic of doing the checking,
        # I just reversed the the list because I know my check_safe function
        # couldn't do the edge case of [3,2,3,4,5] but it does work for [5,4,3,2,3] and removes
        # the one at the end, rather than the start. So it ends up performing the same checks four times.

        print(f"Removing value from levels: {levels[bad_loc]}, bad_loc={bad_loc}")
        levels.pop(bad_loc)
        check_again, bad_loc = check_safe(levels)

        print(
            f"Removing value from rev_levels: {rev_levels[rev_bad_loc]}, rev_bad_loc={rev_bad_loc}"
        )
        rev_levels.pop(rev_bad_loc)
        rev_check_again, rev_bad_loc = check_safe(rev_levels)

        if check_again or rev_check_again:
            num_safe += 1

print(f"Answer: {num_safe}")
