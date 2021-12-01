with open("input.txt") as file:
    input = file.read().strip()
map = input.splitlines()

width = len(map)
repeat_at = len(map[0])
x = 0
y = 0
count = 0
while y < width:
    cord = map[y][x % repeat_at]
    if cord == '#':
        count += 1
    x += 3
    y += 1

print("count of trees: ", count)
