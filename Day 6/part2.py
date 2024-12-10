def find_start_position(map):
    """Find the starting position of the guard, marked by the '^' character."""
    for j in range(len(map[0])):
        for i in range(len(map[j])):

            if map[j][i] == "^":
                return [i, j]

    return [None, None]


def update_direction(direction):
    """Rotate the guard's direction using a -90 deg rotation matrix"""
    return [0 * direction[0] + 1 * direction[1], -1 * direction[0] + 0 * direction[1]]


def display_map(data):
    for line in data:
        print("".join(line))
    print("---------------------------------------")


def clear_X_from_map(data):
    return [["." if char == "X" else char for char in line] for line in data]


# Read in the map data from file
with open("ex_input.txt", "r") as file:
    data = [[char for char in line.rstrip()] for line in file]


# Grid min and max of the grid indices.
x_max = len(data[0]) - 1
x_min = 0
y_max = len(data) - 1
y_min = 0

# Find the initial position of the guard.
last_pos = find_start_position(data)
pos = last_pos.copy()

direction = [0, 1]
print(f"Initial direction: {direction}")

object_to_hit = True
possible_loop = 0
rotate_count = 0

while object_to_hit:

    # If it's within bounds of map and no object in path found yet.
    object_in_path = False
    steps = 0
    while (
        pos[0] <= x_max
        and pos[0] >= 0
        and pos[1] <= y_max
        and pos[1] >= 0
        and not object_in_path
    ):

        # Check if the point we're trying is an obstacle.
        if data[pos[1]][pos[0]] == "#":
            object_in_path = True
            last_pos = [pos[0] - direction[0], pos[1] + direction[1]]

        # Keep track of the path that the guard has taken
        if data[pos[1]][pos[0]] != "X" and not object_in_path:
            data[pos[1]][pos[0]] = "X"

        if pos != last_pos and data[pos[1]][pos[0]] == "X" and rotate_count == 3:
            rotate_count = 0
            possible_loop += 1

            #  # Debugging
            data[pos[1]][pos[0]] = "O"
            display_map(data)
            data[pos[1]][pos[0]] = "."

            data = clear_X_from_map(data)

        # Update the position we're trying.
        if not object_in_path:
            pos = [
                last_pos[0] + steps * direction[0],
                last_pos[1] - steps * direction[1],
            ]
            steps += 1

    if object_in_path:

        # Rotate the direction of the guard
        direction = update_direction(direction)
        rotate_count += 1

        # # Debugging
        # data[last_y_pos][last_x_pos] = "^"
        # display_map(data)

    else:
        object_to_hit = False

    pos = last_pos

# Debugging
# display_map(data)

print(f"Answer: {possible_loop}")
