
def main():
    with open("input.txt") as file:
        input = file.read().strip()

    sequences = input.split('\n')

    largest_seat_id = -1
    for sequence in sequences:
        row_seq = sequence[0:7]
        col_seq = sequence[7:10]
        row = parse_row(row_seq)
        col = parse_col(col_seq)
        seat_id = calc_seat_id(row, col)
        # print(sequence, row, col, seat_id)

        if seat_id > largest_seat_id:
            largest_seat_id = seat_id

    print("largest seat id:", largest_seat_id)


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
