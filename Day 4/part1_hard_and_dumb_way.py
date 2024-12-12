import re


def find_words(line):
    """Find an instance of XMAS in the incoming line."""

    xmas_count = sum(1 for _ in re.finditer(r"XMAS", line))
    samx_count = sum(1 for _ in re.finditer(r"SAMX", line))

    return xmas_count + samx_count


def diagonalize_matrix(data, select):

    n_rows = len(data)
    n_cols = len(data[0])

    size = n_cols + n_rows - 1
    output = [["*" for _ in range(size)] for _ in range(size)]

    if select == "right":
        for i in range(n_rows):
            for j in range(n_cols):
                output[i + j][j] = data[i][j]

    if select == "left":
        for i in range(n_rows):
            for j in range(n_cols):
                output[i + (n_cols - j - 1)][j + n_rows - 1] = data[i][j]

    return output


with open("input.txt", "r") as file:
    data = [list(line.rstrip()) for line in file.readlines()]

# data = [
#     ["a", "b", "c"],
#     ["d", "e", "f"],
#     ["g", "h", "i"],
# ]

word_count = 0

print("--------------------------------------")
print("Horizontal case")
# Horizontal case.
for line in data:
    string_line = "".join(line)
    print(string_line)
    word_count += find_words(string_line)

print("--------------------------------------")
print("Vertical case")
# Verticle_case
data_vertical = [list(row) for row in zip(*data[::-1])]
for line in data_vertical:
    string_line = "".join(line)
    print(string_line)
    word_count += find_words(string_line)

print("--------------------------------------")
print("Right case")
# Diagonal / case
data_diag_right = diagonalize_matrix(data, "right")
for line in data_diag_right:
    string_line = "".join(line)
    print(string_line)
    word_count += find_words(string_line)

print("--------------------------------------")
print("Left case")
# Diagonal \ case
data_diag_left = diagonalize_matrix(data, "left")
for line in data_diag_left:
    string_line = "".join(line)
    print(string_line)
    word_count += find_words(string_line)

print(f"Answer: {word_count}")
