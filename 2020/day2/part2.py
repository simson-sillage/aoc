def pw_valid(password_and_policy: str):
    char, index1, index2, password = pw_parse(password_and_policy)
    count = 0
    if password[index1] == char:
        count += 1
    if password[index2] == char:
        count += 1

    if count != 1:
        return False
    else:
        return True


def pw_parse(password_and_policy: str):
    range, char, password = password_and_policy.split(" ")
    index1, index2 = range.split("-")
    index1 = int(index1) - 1
    index2 = int(index2) - 1
    char = char.replace(':', '')
    return char, index1, index2, password


with open("input.txt") as file:
    input = file.read().strip()
passwords = input.splitlines()

valid = 0
for password in passwords:
    if pw_valid(password):
        valid += 1

print(valid)
