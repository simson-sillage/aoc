import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("error: provide repetitions and path of input file as argument")

    repetitions = int(sys.argv[1])
    with open(sys.argv[2], 'r') as file:
        input = file.read().strip()

    template, rule_inputs = input.split('\n\n')

    rules = {}
    for rule_input in rule_inputs.split('\n'):
        pair, result = rule_input.split(' -> ')
        rules[pair] = result

    quantities = {}
    for c in template:
        quantities[c] = quantities.get(c, 0) + 1

    for i in range(1, len(template), 1):
        pair = template[i - 1] + template[i]
        quantities = add(quantities, apply(pair, rules, 0, repetitions))

    least_common = min(quantities.values())
    most_common = max(quantities.values())

    print(f"quantity difference: {most_common - least_common}")


cache = {}
def apply(pair, rules, current_reps, max_reps):
    quantities = {}
    if current_reps == max_reps:
        return quantities

    global cache
    cached_value = cache.get((pair, current_reps), None)
    if cached_value is not None:
        return cached_value

    result = rules[pair]
    quantities[result] = quantities.get(result, 0) + 1

    pair1 = pair[0] + result
    quant1 = apply(pair1, rules, current_reps + 1, max_reps)
    cache[(pair1, current_reps + 1)] = quant1
    quantities = add(quantities, quant1)

    pair2 = result + pair[1]
    quant2 = apply(pair2, rules, current_reps + 1, max_reps)
    cache[(pair2, current_reps + 1)] = quant2
    quantities = add(quantities, quant2)

    return quantities


def add(d1, d2):
    new = d1.copy()
    for key, value in d2.items():
        new[key] = new.get(key, 0) + value

    return new


main()
