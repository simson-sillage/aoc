import sys
from collections import defaultdict


def main():
    if len(sys.argv) != 2:
        sys.exit("error: provide filename of input as argument")

    with open(sys.argv[1], 'r') as file:
        input = file.read().strip()

    cave_system = defaultdict(set)
    for line in input.split('\n'):
        edge = line.split('-')
        cave_system[edge[0]].add(edge[1])
        cave_system[edge[1]].add(edge[0])

    ways_to_end = find_ways_to_end(cave_system, [], 'start')

    for way in ways_to_end:
        print(way)

    print(f"Number of path through cave: {len(ways_to_end)}")


def find_ways_to_end(cave_system, current_way, current_cave):
    if current_cave == 'end':
        way_to_end = current_way.copy()
        way_to_end.append('end')
        return [way_to_end]

    if current_cave in current_way and current_cave.islower():
        return []

    ways = []
    for next_cave in cave_system[current_cave]:
        next_way = current_way.copy()
        next_way.append(current_cave)
        ways += find_ways_to_end(cave_system, next_way, next_cave)

    return ways


main()
