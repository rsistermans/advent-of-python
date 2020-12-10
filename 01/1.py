import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURR_DIR, "input.txt"), "r") as file:
    numbers = [int(i.strip()) for i in file]

sum = 2020

for i, number in enumerate(numbers[:-1]):
    other_number = sum - number
    if other_number in numbers[i+1:]:
        print("{} times {} equals {}".format(number, other_number, number * other_number))
        break