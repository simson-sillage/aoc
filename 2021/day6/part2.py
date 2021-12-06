import sys


if len(sys.argv) != 3:
    sys.exit("error: provide days and filename of input as argument")

with open(sys.argv[2], 'r') as file:
    input = file.read().strip()

initial_fish = input.split(',')
initial_fish = list(map(int, initial_fish))

fish = {}
for f in initial_fish:
    fish[f] = fish.get(f, 0) + 1

days = int(sys.argv[1])
day = 0
while day < days:
    new_fish = {}

    for index in range(8, 0, -1):
        new_fish[index-1] = fish.get(index, 0)

    new_fish[6] = new_fish.get(6, 0) + fish.get(0, 0)
    new_fish[8] = new_fish.get(8, 0) + fish.get(0, 0)

    fish = new_fish
    day += 1

total_fish = sum(fish.values())

print(f"Total number of fish after {days} days: {total_fish}")
