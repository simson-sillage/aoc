import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

point_inputs, fold_instruction_inputs = input.split('\n\n')

# parse dots
dots = {}
for point_input in point_inputs.split('\n'):
    x, y = point_input.split(',')
    dots[(int(y), int(x))] = True

# parse fold instructions
fold_instructions = []
for instruction in fold_instruction_inputs.split('\n'):
    _, _, relevant = instruction.split(' ')
    axis, value = relevant.split('=')
    fold_instructions.append((axis, int(value)))

# apply fold instructions
for index, instruction in enumerate(fold_instructions):
    axis = instruction[0]
    value = instruction[1]
    new_dots = {}

    if axis == 'x':
        for dot in dots.keys():
            if dot[1] <= value:
                new_dots[dot] = True
            else:
                new_dots[(dot[0], 2 * value - dot[1])] = True
    elif axis == 'y':
        for dot in dots.keys():
            if dot[0] <= value:
                new_dots[dot] = True
            else:
                new_dots[(2 * value - dot[0], dot[1])] = True

    dots = new_dots

    # part1:
    if index == 0:
        print(f"dot count after first fold: {len(new_dots)}")

# part2, print dots, which contain the answer:
print(f"dot count after all folds: {len(new_dots)}")
print("dots:")
y_max = max([dot[0] for dot in dots]) + 1
x_max = max([dot[1] for dot in dots]) + 1
for y in range(y_max):
    for x in range(x_max):
        if new_dots.get((y, x), False):
            print('#', end='')
        else:
            print(' ', end='')
    print()
