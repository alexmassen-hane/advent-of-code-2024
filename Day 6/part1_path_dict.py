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


def display_map(data, path):

    print("---------------------------------------")
    for pos, _ in path.items():
        # print(pos)
        data[pos[1]][pos[0]] = "X"

    for line in data:
        print("".join(line))
    print("---------------------------------------")


# Read in the map data from file
with open("ex_input.txt", "r") as file:
    data = [[char for char in line.rstrip()] for line in file]

# Find the initial position of the guard.
pos = find_start_position(data)
dir = (0, 1)

print(f"Initial position and direction: {pos}, {dir}")
path = {}

object_in_path = True
while object_in_path:

    # If it's within bounds of map and no object in path found yet.
    object_in_path = False
    while is_in_bounds(data, pos) and not object_in_path:

        # Check if the point we're trying is an obstacle.
        if data[pos[1]][pos[0]] == "#":
            object_in_path = True

            # Debugging
            print(f"Found obstical at: {pos}")
            display_map(data, path)

            last_pos = (pos[0] - dir[0], pos[1] + dir[1])

            # Rotate the direction of the guard
            dir = update_direction(dir)

        # Keep track of the path that the guard has taken
        if not pos in path and not object_in_path:
            path[pos] = None

        # Update the position for next iteration.
        pos = (pos[0] + dir[0], pos[1] - dir[1])

    # Update old position to new
    pos = last_pos


# Debugging
display_map(data, path)

for pos, _ in path.items():
    print(pos)

print(f"Answer: {len(path)}")
