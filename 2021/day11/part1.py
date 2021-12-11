import sys
from collections import defaultdict


def main():
    if len(sys.argv) != 2:
        sys.exit("error: provide filename of input as argument")

    with open(sys.argv[1], 'r') as file:
        input = file.read().strip()

    octopi = []
    for line in input.split('\n'):
        octopi.append([int(c) for c in line])

    step = 0
    count = 0
    while step < 100:
        flashed = defaultdict(lambda: False)

        for y, row in enumerate(octopi):
            for x, _ in enumerate(row):
                count += update(octopi, y, x, flashed)

        step += 1

    print(f"count of flashes after {step} steps: {count}")


def update(octopi, y, x, flashed):
    if flashed[(y, x)]:
        return 0
    if octopi[y][x] == 9:
        octopi[y][x] = 0
        flashed[(y, x)] = True
        return update_flash(octopi, y, x, flashed) + 1

    octopi[y][x] += 1
    return 0


def update_flash(octopi, y, x, flashed):
    count = 0

    # check left
    yi = y
    xi = x - 1
    if xi >= 0:
        count += update(octopi, yi, xi, flashed)

    # check left-up
    yi = y - 1
    xi = x - 1
    if xi >= 0 and yi >= 0:
        count += update(octopi, yi, xi, flashed)

    # check up
    yi = y - 1
    xi = x
    if yi >= 0:
        count += update(octopi, yi, xi, flashed)

    # check up-right
    yi = y - 1
    xi = x + 1
    if yi >= 0 and xi < len(octopi[y]):
        count += update(octopi, yi, xi, flashed)

    # check right
    yi = y
    xi = x + 1
    if xi < len(octopi[y]):
        count += update(octopi, yi, xi, flashed)

    # check right-down
    yi = y + 1
    xi = x + 1
    if xi < len(octopi[y]) and yi < len(octopi):
        count += update(octopi, yi, xi, flashed)

    # check down
    yi = y + 1
    xi = x
    if yi < len(octopi):
        count += update(octopi, yi, xi, flashed)

    # check down-left
    yi = y + 1
    xi = x - 1
    if xi >= 0 and yi < len(octopi):
        count += update(octopi, yi, xi, flashed)

    return count


main()
