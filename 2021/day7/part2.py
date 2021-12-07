import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

positions = input.split(',')
positions = list(map(int, positions))

fuel_costs = {}
for candidate in range(min(positions), max(positions) + 1, 1):
    fuel_cost = 0

    for pos in positions:
        diff = abs(candidate-pos)
        fuel_cost += diff * (diff + 1) // 2

    fuel_costs[candidate] = fuel_cost

target = min(fuel_costs, key=fuel_costs.get)
required_fuel = fuel_costs[target]

print(f"cheapest position: {target}")
print(f"required fuel: {required_fuel}")
