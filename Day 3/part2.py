import re

with open("input.txt", "r") as file:
    raw_data = file.readlines()
    data = [line.rstrip() for line in raw_data]

# test = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]


# Define regex definitions
r = re.compile(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)")
r_digits = re.compile(r"\d+")

# At the beginning of the program, mul instructions are enabled.
do_calc = True
total_sum = 0
for line in data:

    # Iterate through all of different 'do()' and 'dont()' cases

    for found in r.finditer(line):
        # Find all the digits in the element and multiply them together

        if found.group() == "do()":
            do_calc = True

        if found.group() == "don't()":
            do_calc = False

        digits = r_digits.findall(found.group())
        if do_calc and digits:
            total_sum += int(digits[0]) * int(digits[1])

print(f"Answer: {total_sum}")
