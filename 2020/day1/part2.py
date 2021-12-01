with open("input.txt") as file:
    input = file.read().strip()
numbers = list(map(int, input.splitlines()))

class Found(Exception): pass
try:
    for i in range(0, len(numbers), 1):
        for j in range(i, len(numbers), 1):
            for k in range(j, len(numbers), 1):
                num1 = numbers[i]
                num2 = numbers[j]
                num3 = numbers[k]
                if num1 + num2 + num3 == 2020:
                    print(num1, " + " , num2, " + ", num3, " equals 2020")
                    print(num1, " * " , num2, " * ", num3, " is ", num1 * num2 * num3)
                    raise Found
except Found:
    pass
