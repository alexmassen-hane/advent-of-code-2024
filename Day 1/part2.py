with open("input.txt", "r") as file:
    cleaned = [line.rstrip().split("   ") for line in file.readlines()]

left = [int(line[0]) for line in cleaned]
right = [int(line[1]) for line in cleaned]

total_sum = 0
for x in left:

    # This can probably be done better with different list notation and counts but I can't be bothered.
    count = 0
    for y in right:
        if x == y:
            count += 1
    total_sum += count * x

print(f"Answer: {total_sum}")
