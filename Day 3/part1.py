import re

with open("input.txt", "r") as file:
    data = [line.rstrip() for line in file.readlines()]

# test = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

# Define regex patterns
r = re.compile(r"mul\(\d+,\d+\)")
r_digits = re.compile(r"\d+")

prod_sum = 0
for line in data:

    # Iterate through all of the 'mult(X,Y)' elements found
    for digits in r.finditer(line):
        # Find all the digits in the element and multiply them together
        prods = r_digits.findall(digits.group())
        prod_sum += int(prods[0]) * int(prods[1])

print(f"Answer: {prod_sum}")
