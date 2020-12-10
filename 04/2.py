import os
import re

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
            propValue = prop.split(":")[1]
            try:
                is_valid = validate_field(propName, propValue)
                if is_valid:
                    required_props.remove(propName)
            except:
                pass
        return len(required_props) == 0
    else:
        return False

def validate_field(name, value):    
    if(name == "byr"):
        try:
            return 1920 <= int(value) <= 2002
        except:
            return False
    elif(name == "iyr"):
        try:
            return 2010 <= int(value) <= 2020
        except:
            return False
    elif(name == "eyr"):
        try:
            return 2020 <= int(value) <= 2030
        except:
            return False
    elif(name == "hgt"):
        try:
            value_type = value[-2:]
            value_number = int(value[:-2])
            if value_type == "cm":
                return 150 <= value_number <= 193
            elif value_type == "in":
                return 59 <= value_number <= 76
            else:
                return False
        except:
            return False
    elif(name == "hcl"):
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
        if match:
            return True
        else:
            return False
    elif(name == "ecl"):
        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        try:
            if eye_colors.index(value) >= 0:
                return True
            else:
                return False
        except:
            return False
    elif(name == "pid"):
        if len(value) == 9:
            try:
                is_number = int(value)
                if is_number:
                    return True
                else:
                    return False
            except:
                return False
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