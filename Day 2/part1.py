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
# data = [[1, 2, 3, 4, 4], [8, 2, 3, 4, 5], [5, 4, 3, 2, 1], [37, 38, 37, 34, 31]]

num_safe = 0
for levels in data:

    print(f"--- New levels ---")
    print(levels)
    rev_levels = levels[::-1]

    check, bad_loc = check_safe(levels)
    if check:
        num_safe += 1

print(f"Answer: {num_safe}")


###
# The below is old garbage that doesn't work
###

# def check_safe(levels):

#     # For a levels list,
#     # Start checking the left and right side of the 1st index.

#     def get_sign(number):
#         return (number > 0) - (number < 0)

#     last_L_diff = levels[1] - levels[0]
#     last_R_diff = levels[2] - levels[1]

#     if abs(last_L_diff) > 3 or abs(last_L_diff) < 1:
#         print(f"last_L_diff not within bounds: {last_L_diff}")
#         return False

#     if abs(last_R_diff) > 3 or abs(last_R_diff) < 1:
#         print(f"last_R_diff not within bounds: {last_R_diff}")
#         return False

#     for i in range(2, len(levels) - 1, 1):
#         # L_diff = levels[i] - levels[i - 1]
#         L_diff = last_R_diff
#         R_diff = levels[i + 1] - levels[i]

#         # Check if all increasing or decreasing
#         if get_sign(last_L_diff) != get_sign(L_diff):
#             print(
#                 f"Sign change: Last L diff and L diff not the same! i={i} {last_L_diff} {L_diff}"
#             )
#             return False

#         elif get_sign(last_R_diff) != get_sign(R_diff):
#             print(
#                 f"Sign change: Last R diff and R diff not the same! i={i} {last_R_diff} {R_diff}"
#             )
#             return False

#         # Check if the differences are within bounds
#         elif abs(L_diff) < 1 or abs(L_diff) > 3:
#             print(f"L_diff not within bounds: i={i} {last_L_diff}")
#             return False

#         elif abs(R_diff) < 1 or abs(R_diff) > 3:
#             print(f"R_diff not within bounds: i={i} {last_R_diff}")
#             return False

#         # Swithc current to last
#         last_L_diff = L_diff
#         last_R_diff = R_diff

#     return True, i


# with open("input.txt", "r") as file:
#     raw_data = file.readlines()

# data = []
# for line in raw_data:
#     cleaned = line.rstrip().split(" ")
#     data.append([int(x) for x in cleaned])

# # test
# # data = [[1, 2, 3, 4, 4], [3, 2, 3, 4, 5], [5, 4, 3, 2, 1]]

# num_safe = 0
# for levels in data:

#     print(f"--- New levels ---")
#     print(levels)

#     # Get the diff of left and right from ith-point.
#     check = check_safe(levels)

#     if check:
#         # Both ways are safe
#         num_safe += 1

# print(f"Answer: {num_safe}")
