with open("input.txt", "r") as file:
    raw_data = file.readlines()

cleaned = [line.rstrip().split("   ") for line in raw_data]

x = [int(line[0]) for line in cleaned]
y = [int(line[1]) for line in cleaned]

x.sort()
y.sort()

total_sum = 0
for xx, yy in zip(x, y):
    total_sum += abs(xx - yy)

print(f"Answer: {total_sum}")
