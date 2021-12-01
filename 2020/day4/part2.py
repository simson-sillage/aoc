import string


def main():
    with open("input.txt") as file:
        input = file.read().strip()

    passports = []
    passport_strings = input.split('\n\n')
    for passport_string in passport_strings:
        kvs = passport_string.split()
        passport = {}
        for kv in kvs:
            key, value = kv.split(':')
            passport[key] = value

        passports.append(passport)

    valid = 0
    for passport in passports:
        if validate(passport):
            valid += 1

    print('valid passports: ', valid)


def validate(passport):
    expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for key in expected_keys:
        value = passport.get(key, None)

        # expected key is missing
        if value is None:
            return False

        # check if field is valid
        if not validate_field(key, value):
            return False

    # all keys are present and have valid fields
    return True


def validate_field(key, value):
    match key:
        case 'byr':
            return int(value) >= 1920 and int(value) <= 2002
        case 'iyr':
            return int(value) >= 2010 and int(value) <= 2020
        case 'eyr':
            return int(value) >= 2020 and int(value) <= 2030
        case 'hgt':
            scalar = value[:-2]
            unit = value[-2:]
            match unit:
                case 'cm':
                    return int(scalar) >= 150 and int(scalar) <= 193
                case 'in':
                    return int(scalar) >= 59 and int(scalar) <= 76
                case _:
                    return False
        case 'hcl':
            if not value[0] == '#':
                return False
            if not len(value[1:]) == 6:
                return False
            return all(char in string.hexdigits for char in value[1:])
        case 'ecl':
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        case 'pid':
            return len(value) == 9 and value.isdecimal()
        case _:
            # ignore unkown fields
            return True


main()
