from itertools import combinations


def main():
    preamble = 25
    with open("input.txt") as file:
        input = file.read().strip()

    sequence = input.split('\n')
    sequence = list(map(int, sequence))

    # find invalid number
    i = preamble
    while i < len(sequence):
        number = sequence[i]
        pairs = combinations(sequence[i-preamble:i], 2)
        if not check(number, pairs):
            invalid_number = number

        i += 1

    print(f"invalid number: {invalid_number}")

    # find sequence that adds up to invalid number
    sum = 0
    start = 0
    for i in range(0, len(sequence)):
        current = sequence[i]

        if current >= invalid_number:
            sum = 0
            start = i + 1
            break

        sum += current

        while sum > invalid_number:
            sum -= sequence[start]
            start += 1

        if sum == invalid_number:
            conseq = sequence[start:i+1]
            break

    print(f"{conseq} add up to {invalid_number}.")

    # encryption weakness:
    print(f"encryption weakness: {min(conseq) + max(conseq)}")


def check(number, pairs):
    for pair in pairs:
        if pair[0] + pair[1] == number:
            return True

    return False


main()
