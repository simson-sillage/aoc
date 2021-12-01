def pw_valid(password_and_policy: str):
    char, min, max, password = pw_parse(password_and_policy)
    count = password.count(char)
    if count < min or count > max:
        return False
    return True


def pw_parse(password_and_policy: str):
    range, char, password = password_and_policy.split(" ")
    min, max = range.split("-")
    min = int(min)
    max = int(max)
    char = char.replace(':', '')
    return char, min, max, password


with open("input.txt") as file:
    input = file.read().strip()
passwords = input.splitlines()

valid = 0
for password in passwords:
    if pw_valid(password):
        valid += 1

print(valid)
