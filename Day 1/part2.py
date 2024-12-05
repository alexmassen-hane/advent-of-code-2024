with open("input.txt", "r") as file:
    raw_data = file.readlines()

cleaned = [line.rstrip().split("   ") for line in raw_data]

left = [int(line[0]) for line in cleaned]
right = [int(line[1]) for line in cleaned]

left.sort()
right.sort()

total_sum = 0
for x in left:

    # This can probably be done better with sets.
    count = 0
    for y in right:
        if x == y:
            count += 1
    total_sum += count * x

print(f"Answer: {total_sum}")
