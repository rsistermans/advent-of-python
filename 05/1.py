import os
import math

# get the file ready
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(CURR_DIR, "input.txt"), "r")
lines = file.read().splitlines()

row_count = 127
col_count = 7

def get_seat_id(row, column):
    return row * 8 + column

def get_boarding_pass(code):
    min_row = 0
    max_row = row_count
    min_col = 0
    max_col = col_count
    for char in code:
        if char == "F":
            max_row = max_row - math.ceil((max_row - min_row) / 2)
        elif char =="B":
            min_row = min_row + math.ceil((max_row - min_row) / 2)
        elif char == "L":
            max_col = max_col - math.ceil((max_col - min_col) / 2)
        elif char == "R":
            min_col = min_col + math.ceil((max_col - min_col) / 2)
    return get_seat_id(min_row, min_col)

boarding_passes = []

for line in lines:
    boarding_passes.append(get_boarding_pass(line))

boarding_passes.sort()

print(boarding_passes[-1:])