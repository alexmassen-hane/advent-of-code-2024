with open("input.txt", "r") as file:
    data = [list(line.rstrip()) for line in file.readlines()]

# What I used for testing
# data = [
#     ["1", "2", "3"],
#     ["M", "b", "S"],
#     ["d", "A", "f"],
#     ["M", "h", "S"],
#     ["4", "5", "6"],
# ]

# Rotate the matrix 3 times
x_count = 0
for rotate in range(1, 5):

    for i, line in enumerate(data[1:-1]):

        # Find all the A's in the row thats not next to the edges
        indexes = [
            j
            for j in range(len(line))
            if line[j] == "A" and j > 0 and j < len(line) - 1
        ]

        # Scan along where the As were found
        for j in indexes:

            # Check both diagonal directions and add to count if works.
            check_down = "".join([data[i][j - 1], data[i + 1][j], data[i + 2][j + 1]])
            check_up = "".join([data[i + 2][j - 1], data[i + 1][j], data[i][j + 1]])
            if check_down == "MAS" and check_up == "MAS":
                x_count += 1

    # Rotate the matrix for next iteration
    data = [list(row) for row in zip(*data[::-1])]

print(f"Answer: {x_count}")
