import sys
from statistics import median


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

positions = input.split(',')
positions = list(map(int, positions))

target = round(median(positions))

total_fuel = 0

for pos in positions:
    total_fuel += abs(target - pos)

print(f"cheapest position: {target}")
print(f"required fuel: {total_fuel}")
