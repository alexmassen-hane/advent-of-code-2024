import re


def find_mults_from_str(line: str):
    prod_sum = 0
    r = re.compile(r"mul\(\d+,\d+\)")
    r_digits = re.compile(r"\d+")

    # Iterate through all of the 'mult(X,Y)' elements found
    for digits in r.finditer(line):
        # Find all the digits in the element and multiply them together
        prods = r_digits.findall(digits.group())
        prod_sum += int(prods[0]) * int(prods[1])

    return prod_sum


with open("input.txt", "r") as file:
    raw_data = file.readlines()
    data = [line.rstrip() for line in raw_data]

total_sum = 0
for line in data:
    total_sum += find_mults_from_str(line)

print(f"Answer: {total_sum}")
