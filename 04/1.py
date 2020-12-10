import os

def read_passports(input: list):
    result = [[]]
    for line in lines:
        if line != "":
            result[-1].extend(line.split())
        else:
            result.append([])
    return result

def validate_passport(passport: list):
    required_props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if len(passport) >= len(required_props):
        for prop in passport:
            propName = prop.split(":")[0]
            try:
                required_props.remove(propName)
            except:
                pass
        return len(required_props) == 0
    else:
        return False
        

# get the file ready
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(CURR_DIR, "input.txt"), "r")
lines = file.read().splitlines()

# read all passports
passports = read_passports(lines)

# validate passport
valid_passports = filter(validate_passport, passports)
valid_passport_count = 0

for passport in valid_passports:
    valid_passport_count += 1

print(len(passports), valid_passport_count)