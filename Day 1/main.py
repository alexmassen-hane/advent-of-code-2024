import numpy as np

with open("input.txt", "r") as file:
    raw_data = file.readlines()

cleaned = [line.rstrip().split("   ") for line in raw_data]
data = np.array(cleaned).astype(int)

x = data[:, 0]
y = data[:, 1]

total_sum = 0
done = 0
x_len = len(x)
for i in range(len(x)):
    x_min_loc = np.argmin(x, axis=0)
    y_min_loc = np.argmin(y, axis=0)

    diff = abs(x[x_min_loc] - y[y_min_loc])
    total_sum += diff
    done += 1

    print(diff, total_sum, x_min_loc, y_min_loc, len(x), done)

    x = np.delete(x, x_min_loc)
    y = np.delete(y, y_min_loc)

print(f"Answer: {total_sum}")
