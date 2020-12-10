import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURR_DIR, "input.txt"), "r") as file:
    tree_map = [i.strip() for i in file]

index = 0
count = 0

for i, tree_line in enumerate(tree_map):
    tree_line_length = len(tree_line)
    char_at_pos = tree_line[index % tree_line_length]
    if char_at_pos == "#":
        count += 1
    index += 3

print(count)