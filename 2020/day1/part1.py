with open("input.txt") as file:
    input = file.read().strip()
numbers = list(map(int, input.splitlines()))

class Found(Exception): pass
try:
    for i in range(0, len(numbers), 1):
        for j in range(i, len(numbers), 1):
            num1 = numbers[i]
            num2 = numbers[j]
            if num1 + num2 == 2020:
                print(num1, " + " , num2, " equals 2020")
                print(num1, " * " , num2, " is ", num1 * num2)
                raise Found
except Found:
    pass
