import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

def is_password_valid(password_line):
    split_password = password_line.split(": ")
    rules = split_password[0]
    password = split_password[1]
    letter = rules.split()[1]
    min_occurrences = int(rules.split()[0].split("-")[0])
    max_occurrences = int(rules.split()[0].split("-")[1])
    occurrences = password.count(letter)
    return min_occurrences <= occurrences <= max_occurrences

with open(os.path.join(CURR_DIR, "input.txt"), "r") as file:
    passwords = [i.strip() for i in file]

valid_passwords = 0

for i, password in enumerate(passwords):
    if is_password_valid(password):
        valid_passwords += 1

print(valid_passwords)