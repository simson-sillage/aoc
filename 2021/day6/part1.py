import sys


if len(sys.argv) != 3:
    sys.exit("error: provide days and filename of input as argument")

with open(sys.argv[2], 'r') as file:
    input = file.read().strip()

fish = input.split(',')
fish = list(map(int, fish))
days = int(sys.argv[1])

day = 0
while day < days:
    new_fish = []

    for index, time in enumerate(fish):
        if time > 0:
            fish[index] = time - 1
        else:
            fish[index] = 6
            new_fish.append(8)

    fish += new_fish
    day += 1

print(f"Total number of fish after {days} days: {len(fish)}")
