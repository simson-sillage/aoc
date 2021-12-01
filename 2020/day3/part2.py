from functools import reduce


def count_trees(map, slope):
    width = len(map)
    repeat_at = len(map[0])
    x = 0
    y = 0
    count = 0
    while y < width:
        cord = map[y][x % repeat_at]
        if cord == '#':
            count += 1
        x += slope[0]
        y += slope[1]

    return count


with open("input.txt") as file:
    input = file.read().strip()
map = input.splitlines()
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = []
for slope in slopes:
    count = count_trees(map, slope)
    counts.append(count)
    print("slope: ", slope)
    print("count of trees: ", count)

answer = reduce((lambda x, y: x * y), counts)
print("The product of tree counts: ", answer)
