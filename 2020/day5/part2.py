from collections import defaultdict


def main():
    with open("input.txt") as file:
        input = file.read().strip()

    sequences = input.split('\n')

    seat_ids = defaultdict(lambda: False)
    largest_seat_id = -1
    for sequence in sequences:
        row_seq = sequence[0:7]
        col_seq = sequence[7:10]
        row = parse_row(row_seq)
        col = parse_col(col_seq)
        seat_id = calc_seat_id(row, col)
        seat_ids[seat_id] = True

        if seat_id > largest_seat_id:
            largest_seat_id = seat_id

    for i in range(1, largest_seat_id):
        if (seat_ids[i] is False and seat_ids[i-1] is True and seat_ids[i+1] is True):
            print("our seat:", i)


def parse_row(sequence):
    return parse(sequence, 127)


def parse_col(sequence):
    return parse(translate(sequence), 7)


def parse(sequence, ceiling):
    floor = 0
    for instruction in sequence:
        match instruction:
            case 'F':
                ceiling = ceiling - 1 - (ceiling - floor) // 2
            case 'B':
                floor = floor + 1 + (ceiling - floor) // 2
            case _:
                raise ValueError(f"illegal instruction: {instruction}")

    if floor == ceiling:
        return floor
    else:
        raise RuntimeError(f"illegal state reached: {sequence}")


def translate(sequence):
    answer = []
    for instruction in sequence:
        match instruction:
            case 'L':
                answer.append('F')
            case 'R':
                answer.append('B')

    return ''.join(answer)


def calc_seat_id(row, col):
    return row * 8 + col


main()
