import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

values = {}
values[')'] = 1
values[']'] = 2
values['}'] = 3
values['>'] = 4

scores = []
for line in input.split('\n'):
    corrupted = False
    open_braces = []

    for c in line:
        match c:
            case('(' | '{' | '<' | '['):
                open_braces.append(c)
                continue
            case ')':
                to_check = '('
            case '}':
                to_check = '{'
            case '>':
                to_check = '<'
            case ']':
                to_check = '['
            case _:
                raise ValueError(c)

        closed_brace = open_braces.pop()
        if closed_brace != to_check:
            corrupted = True
            break

    # ignore corrupted lines
    if corrupted:
        continue

    closing_sequence = []
    for brace in reversed(open_braces):
        match brace:
            case '(':
                closing_sequence.append(')')
            case '{':
                closing_sequence.append('}')
            case '<':
                closing_sequence.append('>')
            case '[':
                closing_sequence.append(']')
            case _:
                raise ValueError(brace)

    print(f"{line} requires {closing_sequence}")

    score = 0
    for brace in closing_sequence:
        score = 5 * score + values[brace]
    scores.append(score)


print(f"score: {sorted(scores)[len(scores)//2]}")
