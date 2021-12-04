import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("error: provide filename of input as argument")

    with open(sys.argv[1], 'r') as file:
        input = file.read().strip()

    binary_numbers = input.split()
    length = len(binary_numbers[0])

    oxygen = binary_numbers
    for row in range(0, length, 1):
        bit = most_common_bit_per_row(oxygen, row)
        oxygen = filter_by_bit_and_row(oxygen, bit, row)

        if len(oxygen) <= 1:
            break

    co2 = binary_numbers
    for row in range(0, length, 1):
        bit = invert(most_common_bit_per_row(co2, row))
        co2 = filter_by_bit_and_row(co2, bit, row)

        if len(co2) <= 1:
            break

    print(f"oxygen: {oxygen[0]}, {int(oxygen[0], 2)}")
    print(f"co2: {co2[0]}, {int(co2[0], 2)}")
    print(f"oxygen * co2: {int(oxygen[0], 2) * int(co2[0], 2)}")


def filter_by_bit_and_row(binary_numbers, bit, row):
    result = []
    for num in binary_numbers:
        if num[row] == bit:
            result.append(num)

    return result


def most_common_bit_per_row(binary_numbers, row):
    zeroes = 0
    ones = 0
    for num in binary_numbers:
        bit = num[row]
        if bit == '0':
            zeroes += 1
        elif bit == '1':
            ones += 1
        else:
            raise ValueError

    if zeroes > ones:
        return '0'
    else:
        return '1'


def invert(bit):
    if bit == '0':
        return '1'
    elif bit == '1':
        return '0'
    else:
        raise ValueError


main()
