# 'cid' optional
expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open("input.txt") as file:
    input = file.read().strip()

# parse passports
passports = []
passport_strings = input.split('\n\n')
for passport_string in passport_strings:
    kvs = passport_string.split()
    passport = {}
    for kv in kvs:
        key, value = kv.split(':')
        passport[key] = value

    passports.append(passport)

# count valid passports
valid = 0
for passport in passports:
    missing = set(expected_keys) - set(list(passport.keys()))
    if len(missing) == 0:
        valid += 1

print('valid passports: ', valid)
