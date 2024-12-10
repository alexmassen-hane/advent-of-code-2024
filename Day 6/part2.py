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
        for pos, _ in path.items():
            # print(pos)
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

    pos = copy.deepcopy(initial_pos)
    dir = (0, 1)

    print(f"Initial position and direction: {pos}, {dir}")
    path = {}
    trajectory = {}
    closed_loop_pos = {}

    display_map(data)

    object_in_path = True
    while object_in_path:

        # If it's within bounds of map and no object in path found yet.
        object_in_path = False
        while is_in_bounds(data, pos) and not object_in_path:

            # Check if it's a closed loop
            if (
                (pos, update_direction(dir)) in trajectory
                and not object_in_path
                and not pos in closed_loop_pos
            ):
                closed_loop_pos[pos] = None

            # Check if the point we're trying is an obstacle.
            if data[pos[1]][pos[0]] == "#" or data[pos[1]][pos[0]] == "O":
                object_in_path = True

                # The last position of the guard is 1 step back from the current position.
                last_pos = (pos[0] - dir[0], pos[1] + dir[1])

                # display_map(data, trajectory)

                # Rotate the direction of the guard
                dir = update_direction(dir)

            # Keep track of the path that the guard has taken
            if not pos in path and not object_in_path and is_in_bounds(data, pos):
                path[pos] = dir
                trajectory[(pos, dir)] = None

            # Update the position for next iteration.
            pos = (pos[0] + dir[0], pos[1] - dir[1])

        # Update old position to new
        pos = last_pos

    display_map(data, path)

    # Return a dictionary of positions and direction pairs.
    return path, closed_loop_pos


def check_for_closed_loop(data, initial_pos, closed_loop_pos, O_point=None):

    pos = copy.deepcopy(initial_pos)
    dir = (0, 1)

    print(f"Initial position and direction: {pos}, {dir}")
    path = {}
    trajectory = {}

    closed_loop_pos = {}

    object_in_path = True
    while object_in_path and not O_point:

        # If it's within bounds of map and no object in path found yet.
        object_in_path = False
        while is_in_bounds(data, pos) and not object_in_path:

            # Keep track of the path that the guard has taken
            if not (pos, dir) in trajectory and not object_in_path:
                path[pos] = None
                trajectory[(pos, dir)] = None

            # Check if it's a closed loop
            if (
                (pos, update_direction(dir)) in trajectory
                and not object_in_path
                and pos not in closed_loop_pos
            ):
                closed_loop_pos[pos] = None

                display_map(data, path, loop_point=pos)

                return closed_loop_pos

            # Check if the point we're trying is an obstacle.
            if data[pos[1]][pos[0]] == "#" or data[pos[1]][pos[0]] == "O":
                object_in_path = True

                # The last position of the guard is 1 step back from the current position.
                last_pos = (pos[0] - dir[0], pos[1] + dir[1])

                # Rotate the direction of the guard
                dir = update_direction(dir)

            # Update the position for next iteration.
            pos = (pos[0] + dir[0], pos[1] - dir[1])

        # Update old position to new
        pos = last_pos

    return closed_loop_pos


# Read in the map data from file
with open("ex_input.txt", "r") as file:
    data = [[char for char in line.rstrip()] for line in file]

initial_pos = find_start_position(data)
# Find the path that the guard takes.
path_taken, closed_loop_pos = find_path(data, initial_pos)
print(f"Length of the path taken by the guard: {len(path_taken)}")

# display_map(data)
# display_map(data, path_taken)

# Recheck every point that the guard takes.

# Find all close loops that aren't by adding extras in paths.
# closed_loop_pos.update(check_for_closed_loop(data, initial_pos, closed_loop_pos))
for pos, dir in path_taken.items():

    print(f"Position and direction pair: {pos}, {dir}")

    check_pos = (pos[0] + dir[0], pos[1] - dir[1])
    if data[pos[1]][pos[0]] != "^" and data[check_pos[1]][check_pos[0]] != "#":
        print(f"Now checking point: {check_pos}, count: {len(closed_loop_pos)}")

        # Put a blockage in the way of the guard and check if it causes a closed loop.
        data[check_pos[1]][check_pos[0]] = "O"

        closed_loop_pos.update(
            check_for_closed_loop(data, initial_pos, closed_loop_pos)
        )

        # display_map(data, None, check_pos)

        # if check_for_closed_loop(data):
        #     count += 1

        data[check_pos[1]][check_pos[0]] = "."

# check_pos = (6, 1)
# print(f"Now checking point: {check_pos}")

# if data[check_pos[1]][check_pos[0]] != "^":
#     data[check_pos[1]][check_pos[0]] = "#"

#     count += check_for_closed_loop(data)

print(f"Answer: {len(closed_loop_pos)}")
