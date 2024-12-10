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


# Read in the map data from file
with open("input.txt", "r") as file:
    data = [[char for char in line.rstrip()] for line in file]


# Grid min and max of the grid indices.
x_max = len(data[0]) - 1
x_min = 0
y_max = len(data) - 1
y_min = 0

# Find the initial position of the guard.
last_pos = find_start_position(data)

direction = [0, 1]
print(f"Initial direction: {direction}")

object_to_hit = True
position_count = 0

while object_to_hit:

    pos = last_pos

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
            position_count += 1
            data[pos[1]][pos[0]] = "X"

        # Update the position we're trying.
        pos = [
            last_pos[0] + steps * direction[0],
            last_pos[1] - steps * direction[1],
        ]
        steps += 1

    if object_in_path:

        # Rotate the direction of the guard
        direction = update_direction(direction)

        # # Debugging
        # data[last_y_pos][last_x_pos] = "^"
        # display_map(data)

    else:
        object_to_hit = False

# Debugging
# display_map(data)

print(f"Answer: {position_count}")
