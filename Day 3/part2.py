import re

with open("input.txt", "r") as file:
    data = [line.rstrip() for line in file.readlines()]

# test = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


# Define regex patterns
r = re.compile(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)")
r_digits = re.compile(r"\d+")

# At the beginning of the program, mul instructions are enabled.
do_calc = True
total_sum = 0
for line in data:

    # Iterate through all of different 'do()', 'dont()' and 'mult(X,Y)' cases
    for found in r.finditer(line):

        if found.group() == "do()":
            do_calc = True

        if found.group() == "don't()":
            do_calc = False

        # Only perform the calc if it's preceeded with a 'do()'
        digits = r_digits.findall(found.group())
        if do_calc and digits:
            total_sum += int(digits[0]) * int(digits[1])

print(f"Answer: {total_sum}")
