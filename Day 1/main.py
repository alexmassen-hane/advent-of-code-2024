with open("input.txt", "r") as file:
    raw_data = file.readlines()

cleaned = [line.rstrip().split("   ") for line in raw_data]

x = []
y = []
for line in cleaned:
    x.append(int(line[0]))
    y.append(int(line[1]))

total_sum = 0
done = 0
for i in range(len(x)):
    x_min_loc = x.index(min(x))
    y_min_loc = y.index(min(y))

    diff = abs(x[x_min_loc] - y[y_min_loc])
    total_sum += diff
    done += 1

    print(diff, total_sum, x_min_loc, y_min_loc, len(x), done)

    x.pop(x_min_loc)
    y.pop(y_min_loc)

print(f"Answer: {total_sum}")
