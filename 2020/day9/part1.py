from itertools import combinations


def main():
    preamble = 25
    with open("input.txt") as file:
        input = file.read().strip()

    sequence = input.split('\n')
    sequence = list(map(int, sequence))

    index = preamble
    while index < len(sequence):
        number = sequence[index]
        pairs = combinations(sequence[index-preamble:index], 2)
        if not check(number, pairs):
            print(f"no pair adds up to {number}.")

        index += 1


def check(number, pairs):
    for pair in pairs:
        if pair[0] + pair[1] == number:
            return True

    return False


main()
