import sys


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
        flashed = {}

        for y, row in enumerate(octopi):
            for x, _ in enumerate(row):
                count += update(octopi, y, x, flashed)

        step += 1

    print(f"count of flashes after {step} steps: {count}")


def update(octopi, y, x, flashed):
    # out of bounds
    if x < 0 or y < 0 or y >= len(octopi) or x >= len(octopi[y]):
        return 0
    if flashed.get((y, x), False):
        return 0
    if octopi[y][x] == 9:
        octopi[y][x] = 0
        flashed[(y, x)] = True
        return update_flash(octopi, y, x, flashed) + 1

    octopi[y][x] += 1
    return 0


def update_flash(octopi, y, x, flashed):
    count = 0

    count += update(octopi, y, x - 1, flashed)  # left
    count += update(octopi, y - 1, x - 1, flashed)  # left-up
    count += update(octopi, y - 1, x, flashed)  # up
    count += update(octopi, y - 1, x + 1, flashed)  # up-right
    count += update(octopi, y, x + 1, flashed)  # right
    count += update(octopi, y + 1, x + 1, flashed)  # right-down
    count += update(octopi, y + 1, x, flashed)  # down
    count += update(octopi, y + 1, x - 1, flashed)  # down-left

    return count


main()
