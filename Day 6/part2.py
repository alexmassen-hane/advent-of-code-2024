import copy


def find_start_position(map):
    """Find the starting position of the guard, marked by the '^' character."""
    for j in range(len(map[0])):
        for i in range(len(map[j])):

            if map[j][i] == "^":
                return (i, j)

    return (None, None)


def update_direction(dir):
    """Rotate the guard's direction using a -90 deg rotation matrix"""
    return (0 * dir[0] + 1 * dir[1], -1 * dir[0] + 0 * dir[1])


def is_in_bounds(data, pos):
    """Check if the position of the guard is within the bounds of the grid."""
    return (
        pos[0] <= len(data[0]) - 1
        and pos[0] >= 0
        and pos[1] <= len(data) - 1
        and pos[1] >= 0
    )


def display_map(data, path=None, O_point=None, loop_point=None):

    display = copy.deepcopy(data)

    print("---------------------------------------")
    if path:
        for pos in path.keys():
            if display[pos[1]][pos[0]] != "^":
                display[pos[1]][pos[0]] = "X"

    if O_point:
        display[O_point[1]][O_point[0]] = "O"

    if loop_point:
        display[loop_point[1]][loop_point[0]] = "%"

    for line in display:
        print("".join(line))

    if loop_point:
        display[loop_point[1]][loop_point[0]] = "."
    print("---------------------------------------")


def find_path(data, initial_pos):
    """Find the path that the guard takes"""

    guard_pos = copy.deepcopy(initial_pos)
    dir = (0, 1)

    print(f"Initial position and direction: {guard_pos}, {dir}")
    path = {}

    # display_map(data, path)
    # print(path)

    while is_in_bounds(data, guard_pos):

        # Keep track of the path that the guard has taken
        path[guard_pos] = None
        check_ahead = (guard_pos[0] + dir[0], guard_pos[1] - dir[1])

        if is_in_bounds(data, check_ahead):
            # Check if the point we're trying is an obstacle.
            if data[check_ahead[1]][check_ahead[0]] == "#":
                # Rotate the direction of the guard
                dir = update_direction(dir)
        else:

            # The check ahead is not in the map, therefore out of bounds and should exit the loop.

            # display_map(data, path)
            # print(path)

            return path

        # Update the position of the guard for next iteration.
        guard_pos = (guard_pos[0] + dir[0], guard_pos[1] - dir[1])

        # display_map(data, path)
        # print(path)


def check_if_closed_loop(data, initial_pos, check_pos=None):
    """Find the path that the guard takes"""

    guard_pos = copy.deepcopy(initial_pos)
    dir = (0, 1)

    print(f"Initial position and direction: {guard_pos}, {dir}")
    path = {}
    trajectory = {}

    display_map(data, path)
    print(path)

    while is_in_bounds(data, guard_pos):

        # Keep track of the path that the guard has taken
        path[guard_pos] = dir
        trajectory[(guard_pos, dir)] = 0

        check_ahead = (guard_pos[0] + dir[0], guard_pos[1] - dir[1])

        # Guard has been here before. This is a loop.
        if (guard_pos, update_direction(dir)) in trajectory:

            trajectory[(guard_pos, update_direction(dir))] += 1
            print(
                f"Found {trajectory[(guard_pos, update_direction(dir))]} loop/s at: {guard_pos}"
            )

            # Guard is going in an infinite loop - need to exit.
            if trajectory[(guard_pos, update_direction(dir))] > 1:
                print(f"Infinite loop found {(guard_pos, dir)}")
                display_map(data, path)

                if check_pos == guard_pos:
                    return 1
                else:
                    return 0

        if is_in_bounds(data, check_ahead):
            # Check if the point we're trying is an obstacle.
            if data[check_ahead[1]][check_ahead[0]] == "#":
                # Rotate the direction of the guard
                dir = update_direction(dir)
        else:
            # The check ahead is not in the map, therefore out of bounds and should exit the loop.
            display_map(data, path)
            # print(path)
            print(f"Exiting the map! ")
            return 0

        # Update the position of the guard for next iteration.
        guard_pos = (guard_pos[0] + dir[0], guard_pos[1] - dir[1])

        display_map(data, path)
        # print(path)


# Read in the map data from file
with open("ex_input.txt", "r") as file:
    data = [[char for char in line.rstrip()] for line in file]

# Find the initial position of the guard from the ^ character
initial_pos = find_start_position(data)
path_taken = find_path(data, initial_pos)
print(f"Length of the path taken by the guard: {len(path_taken)}")

# A test case for an infinite loop
pos = (3, 6)
dir = (0, 1)
check_pos = pos
loop_count = 0
data[check_pos[1]][check_pos[0]] = "#"

loop_count += check_if_closed_loop(data, initial_pos, check_pos)

data[check_pos[1]][check_pos[0]] = "."

# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# loop_count = 0
# for pos, dir in path_taken.items():

#     print(pos)

#     # check_pos = (pos[0] + dir[0], pos[1] - dir[1])

#     if data[pos[1]][pos[0]] != "#":

#         data[pos[1]][pos[0]] = "#"

#         loop_count += check_if_closed_loop(data, initial_pos, pos)

#         data[pos[1]][pos[0]] = "."

#         print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print(f"Answer: {loop_count}")
