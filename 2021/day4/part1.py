import sys


class Field():
    def __init__(self, value):
        self.value = value
        self.marked = False


def main():
    if len(sys.argv) != 2:
        sys.exit("error: provide filename of input as argument")

    with open(sys.argv[1], 'r') as file:
        input = file.read().strip().split('\n\n')

    numbers = input[0].split(',')
    board_inputs = input[1:]

    boards = parse(board_inputs)
    for number in numbers:
        mark(boards, number)
        winner = check(boards)
        if winner is not None:
            break

    pprint(winner)
    score = calc_score(winner)
    print(f"score: {score}")
    print(f"final number: {number}")
    print(f"final score: {score * int(number)}  ")


def parse(inputs):
    boards = []
    for input in inputs:
        values = iter(input.split())
        board = []
        for x in range(0, 5, 1):
            row = []
            for y in range(0, 5, 1):
                field = Field(next(values))
                row.append(field)

            board.append(row)
        boards.append(board)

    return boards


def mark(boards, number):
    for board in boards:
        for row in board:
            for field in row:
                if field.value == number:
                    field.marked = True


def check(boards):
    for board in boards:
        for row in board:
            won = True
            for field in row:
                if not field.marked:
                    won = False
                    break
            if won:
                return board

        for column in range(0, 5, 1):
            won = True
            for row in board:
                field = row[column]
                if not field.marked:
                    won = False
                    break
            if won:
                return board

    return None


def pprint(board):
    bold = '\033[1m'
    end = '\033[0m'
    for row in board:
        for field in row:
            if field.marked:
                print(bold + f"{field.value:2}" + end, end=' ')
            else:
                print(f"{field.value:2}", end=' ')
        print()


def calc_score(board):
    score = 0
    for row in board:
        for field in row:
            if not field.marked:
                score += int(field.value)
    return score


main()
