import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("error: provide filename of input as argument")

    with open(sys.argv[1], 'r') as file:
        input = file.read().strip()

    cave = []
    for line in input.split('\n'):
        cave.append([int(c) for c in line])

    basin_sizes = []
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

            # low point found, calculate basin size
            basin_sizes.append(calc_basin_size(cave, y, x, {}))

    basin_sizes = sorted(basin_sizes)
    product = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

    print(f"basin sizes: {basin_sizes}")
    print(f"Product of three largest basin sizes: {product}")


def calc_basin_size(cave, y, x, skip):
    if cave[y][x] == 9:
        return 0
    if skip.get((y, x), False):
        return 0

    count = 1
    skip[(y, x)] = True

    # check left
    if x - 1 >= 0:
        count += calc_basin_size(cave, y, x - 1, skip)

    # check right
    if x + 1 < len(cave[y]):
        count += calc_basin_size(cave, y, x + 1, skip)

    # check up
    if y - 1 >= 0:
        count += calc_basin_size(cave, y - 1, x, skip)

    # check down
    if y + 1 < len(cave):
        count += calc_basin_size(cave, y + 1, x, skip)

    return count


main()
