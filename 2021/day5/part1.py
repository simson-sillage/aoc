import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    inputs = file.read().strip().split('\n')

lines = []
for input in inputs:
    start_cords, _, end_cords = input.split(' ')
    x0, y0 = start_cords.split(',')
    x1, y1 = end_cords.split(',')
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    # consider only horizontal or vertical lines
    if not (x0 == x1 or y0 == y1):
        continue

    line = set()
    for i in range(0, abs(x1-x0)+1, 1):
        point = (min(x0, x1) + i, y0)
        line.add(point)
    for i in range(0, abs(y1-y0)+1, 1):
        point = (x0, min(y0, y1) + i)
        line.add(point)

    lines.append(line)

count = {}
for line in lines:
    for point in line:
        count[point] = count.get(point, 0) + 1

count_overlapping_points = 0
for point, counter in count.items():
    if counter >= 2:
        count_overlapping_points += 1

print(f"count of points with overlap: {count_overlapping_points}")
