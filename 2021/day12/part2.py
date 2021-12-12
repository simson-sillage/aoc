import sys
from collections import defaultdict, Counter


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

    print(f"Number of path through cave: {len(ways_to_end)}")


def find_ways_to_end(cave_system, current_way, current_cave):
    if current_cave == 'end':
        way_to_end = current_way.copy()
        way_to_end.append('end')
        return [way_to_end]

    # start can't be visited twice
    if current_cave == 'start' and 'start' in current_way:
        return []

    if current_cave in current_way and current_cave.islower():
        # check if a small cave was visited twice already
        small_caves_visited = [cave for cave in current_way if cave.islower()]
        if max(Counter(small_caves_visited).values()) > 1:
            return []
        else:  # allow one duplicate small cave
            pass

    ways = []
    for next_cave in cave_system[current_cave]:
        next_way = current_way.copy()
        next_way.append(current_cave)
        ways += find_ways_to_end(cave_system, next_way, next_cave)

    return ways


main()
