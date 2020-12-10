import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURR_DIR, "input.txt"), "r") as file:
    numbers = [int(i.strip()) for i in file]

sum = 2020

for i, number_1 in enumerate(numbers[:-1]):
    for j, number_2 in enumerate(numbers[:-1]):
        for k, number_3 in enumerate(numbers[:-1]):
            if(number_1 + number_2 + number_3 == sum):
                print("Got it: {} x {} x {} = {}".format(number_1, number_2, number_3, number_1 * number_2 * number_3))