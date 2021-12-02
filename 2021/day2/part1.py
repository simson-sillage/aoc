def main():
    with open("input.txt") as file:
        input = file.read().strip()

    commands = input.split('\n')

    # starting positions:
    x = 0
    y = 0

    for command in commands:
        x, y = updatePosition(x, y, *parseCommand(command))

    print(f"x: {x}")
    print(f"y: {y}")
    print(f"product: {x*y}")


def parseCommand(command):
    direction, magnitude = command.split()
    magnitude = int(magnitude)
    match direction:
        case "forward":
            return magnitude, 0
        case "down":
            return 0, -magnitude
        case "up":
            return 0, +magnitude
        case _:
            raise ValueError


def updatePosition(x0, y0, delta_x, delta_y):
    return x0 + delta_x, y0 + delta_y


main()
