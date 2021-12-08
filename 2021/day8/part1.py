import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

count = 0
for line in input.split('\n'):
    output_values = line.split('|')[1].strip().split(' ')
    for value in output_values:
        if len(value) in [2, 3, 4, 7]:
            count += 1

print(f"count of 1, 4, 7, 8: {count}")
