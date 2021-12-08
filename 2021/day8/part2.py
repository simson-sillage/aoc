import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("error: provide filename of input as argument")

    with open(sys.argv[1], 'r') as file:
        input = file.read().strip()

    sum = 0
    for line in input.split('\n'):
        input, output = [part.strip() for part in line.split('|')]
        input_values = [''.join(sorted(i)) for i in input.split(' ')]
        output_values = [''.join(sorted(o)) for o in output.split(' ')]

        mapping = map_to_numbers(input_values)

        sum += (1000 * mapping[output_values[0]]
                + 100 * mapping[output_values[1]]
                + 10 * mapping[output_values[2]]
                + mapping[output_values[3]])

    print(f"sum of all output values: {sum}")


def map_to_numbers(values):
    mapping = {}

    for v in values:
        match len(v):
            case 2:
                mapping[v] = 1
                mapping[1] = v
            case 3:
                mapping[v] = 7
                mapping[7] = v
            case 4:
                mapping[v] = 4
                mapping[4] = v
            case 7:
                mapping[v] = 8
                mapping[8] = v
            case _:
                continue

    three_identifier = set(mapping[1]).intersection(set(mapping[7]))
    for v in values:
        # 3 shares two segments with 1 and 7
        if len(v) == 5 and len(set(v).intersection(three_identifier)) == 2:
            mapping[v] = 3
            mapping[3] = v
        # 6 and 1 have only one segment in common
        elif len(v) == 6 and len(set(v).intersection(set(mapping[1]))) == 1:
            mapping[v] = 6
            mapping[6] = v
        # 4 and 9 have 4 segements in common
        elif len(v) == 6 and len(set(v).intersection(set(mapping[4]))) == 4:
            mapping[v] = 9
            mapping[9] = v
        # 4 and 0 have 3 segements in common
        elif len(v) == 6 and len(set(v).intersection(set(mapping[4]))) == 3:
            mapping[v] = 0
            mapping[0] = v

    for v in values:
        # 5 and 6 have 5 segments in common
        if len(v) == 5 and len(set(v).intersection(set(mapping[6]))) == 5:
            mapping[v] = 5
            mapping[5] = v

    for v in values:
        # only one mapping remaining, 2:
        if v not in mapping:
            mapping[v] = 2
            mapping[2] = v

    return mapping


main()
