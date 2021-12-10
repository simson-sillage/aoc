import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

error_values = {}
error_values[')'] = 3
error_values[']'] = 57
error_values['}'] = 1197
error_values['>'] = 25137

score = 0
for line in input.split('\n'):
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
            print(f"illegal brace found: {c}, line: {line}")
            score += error_values[c]
            break

print(f"score: {score}")
