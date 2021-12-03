with open("input.txt") as file:
    input = file.read().strip()

binary_numbers = input.split()
length = len(binary_numbers[0])

gamma = ""
epsilon = ""

# iterate over bits:
for i in range(0, length, 1):
    zeroes = 0
    ones = 0
    for num in binary_numbers:
        match num[i]:
            case '0':
                zeroes += 1
            case '1':
                ones += 1
            case _:
                raise ValueError

    if zeroes > ones:
        gamma += '0'
        epsilon += '1'
    elif ones > zeroes:
        gamma += '1'
        epsilon += '0'
    else:
        raise ValueError

print(f"gamma: {gamma}, {int(gamma, 2)}")
print(f"epsilon: {epsilon}, {int(epsilon, 2)}")
print(f"gamma * epsilon: {int(gamma, 2) * int(epsilon, 2)}")
