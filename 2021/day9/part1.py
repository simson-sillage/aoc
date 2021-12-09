import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

cave = []
for line in input.split('\n'):
    cave.append([int(c) for c in line])

total_risk = 0
for y, row in enumerate(cave):
    for x, height in enumerate(row):
        left = row[x-1] if x >= 1 else None
        right = row[x+1] if x < len(row) - 1 else None
        up = cave[y-1][x] if y >= 1 else None
        down = cave[y+1][x] if y < len(cave) - 1 else None

        if left is not None and left <= height:
            continue
        if right is not None and right <= height:
            continue
        if up is not None and up <= height:
            continue
        if down is not None and down <= height:
            continue

        # low point found
        total_risk += (height + 1)

print(f"accumulated risk of low points: {total_risk}")
