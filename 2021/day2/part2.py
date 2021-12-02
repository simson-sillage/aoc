with open("input.txt") as file:
    input = file.read().strip()

commands = input.split('\n')

# starting positions:
horizontal = 0
depth = 0
aim = 0

for command in commands:
    direction, magnitude = command.split()
    magnitude = int(magnitude)
    match direction:
        case "forward":
            horizontal += magnitude
            depth += aim * magnitude
        case "down":
            aim += magnitude
        case "up":
            aim -= magnitude
        case _:
            raise ValueError

print(f"horizontal: {horizontal}")
print(f"depth: {depth}")
print(f"product: {horizontal*depth}")
