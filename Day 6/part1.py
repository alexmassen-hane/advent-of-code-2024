def find_start_position(map):
    """Find the starting position of the guard, marked at the '^' character."""
    for j in range(len(map[0])):
        for i in range(len(map[j])):

            if map[j][i] == "^":
                return [i, j]

    return [None, None]


def rotate_direction(direction):
    """Rotate the guard using a -90 deg rotation matrix"""

    x_new = 0 * direction[0] + 1 * direction[1]
    y_new = -1 * direction[0] + 0 * direction[1]

    return [x_new, y_new]


def display_map(data):
    for line in data:
        print("".join(line))


# Read in the map data from file
with open("input.txt", "r") as file:
    data = [[char for char in line.rstrip()] for line in file]
    # data = [line.rstrip() for line in file]


# Max grid in data list of lists
x_max = len(data[0]) - 1
x_min = 0
y_max = len(data) - 1
y_min = 0

print(f"x_max = {x_max}, y_max = {y_max}")

display_map(data)
print("---------------------------------------")


# Find the initial position of the guard. Don't need to worry about the direction it's facing initially.
# It is always up.
last_x_pos, last_y_pos = find_start_position(data)
# last_pos = find_start_position(data)


direction = [0, 1]
print(f"Initial direction: {direction}")

object_to_hit = True
hit_count = 1
position_count = 0

while object_to_hit:

    # pos_try = last_pos
    x_try = last_x_pos
    y_try = last_y_pos

    # If it's within bounds of map and no object in path found let.
    object_in_path = False
    steps = 0
    while (
        x_try <= x_max
        and x_try >= 0
        and y_try <= y_max
        and y_try >= 0
        and not object_in_path
    ):
        # while (
        #     pos_try[0] <= x_max
        #     and pos_try[0] >= 0
        #     and pos_try[1] <= y_max
        #     and pos_try[1] >= 0
        #     and not object_in_path
        # ):

        # print(f"x_delta = {x_delta}, y_delta = {y_delta}")
        # print(f"x_try = {x_try}, y_try = {y_try}, steps={steps}")

        if data[y_try][x_try] == "#":
            # print(f"Object in path at x: {x_try} y: {y_try}")
            object_in_path = True
            # last_pos = [pos_try[0] - direction[0], pos_try[1] + direction[1]]
            last_x_pos = x_try - direction[0]
            last_y_pos = y_try + direction[1]

        if data[y_try][x_try] != "X" and not object_in_path:
            position_count += 1
            data[y_try][x_try] = "X"

        # if data[y_try][x_try] != "X" and not object_in_path and direction == loop_direction:

        # put update at end
        # pos_try = [
        #     last_pos[0] + steps * direction[0],
        #     last_pos[1] + steps * direction[1],
        # ]
        x_try = last_x_pos + steps * direction[0]
        y_try = last_y_pos - steps * direction[1]
        steps += 1

    if object_in_path:

        # Rotate the direction of the guard
        direction = rotate_direction(direction)

        # # Debugging
        # data[last_y_pos][last_x_pos] = "^"
        # display_map(data)
        print("---------------------------------------")

    else:
        object_to_hit = False

display_map(data)
print("---------------------------------------")
print(f"Answer: {position_count}")
