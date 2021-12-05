import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

commands = input.split('\n')

horizontal = 0
depth = 0

for command in commands:
    direction, magnitude = command.split()
    magnitude = int(magnitude)
    match direction:
        case "forward":
            horizontal += magnitude
        case "down":
            depth += magnitude
        case "up":
            depth -= magnitude
        case _:
            raise ValueError

print(f"x: {horizontal}")
print(f"y: {depth}")
print(f"product: {horizontal*depth}")
