import sys


if len(sys.argv) != 2:
    sys.exit("error: provide filename of input as argument")

with open(sys.argv[1], 'r') as file:
    input = file.read().strip()

template, rule_inputs = input.split('\n\n')

rules = {}
for rule_input in rule_inputs.split('\n'):
    pair, result = rule_input.split(' -> ')
    rules[pair] = result

# apply rules
result = template
for repitions in range(10):
    new_result = result[0]

    for i in range(1, len(result), 1):
        pair = result[i - 1] + result[i]
        new_result += rules[pair] + pair[1]

    result = new_result

# count occurances
occurances = {}
for c in result:
    occurances[c] = occurances.get(c, 0) + 1

least_common = min(occurances.values())
most_common = max(occurances.values())

print(f"occurance difference: {most_common - least_common}")
