import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURR_DIR, "input.txt"), "r") as file:
    tree_map = [i.strip() for i in file]

x = [1, 3, 5, 7, 1]
y = [1, 1, 1, 1, 2]

def count_trees(x, y):
    index = 0
    count = 0
    for i, tree_line in enumerate(tree_map):
        if i % y == 0:
            tree_line_length = len(tree_line)
            char_at_pos = tree_line[index % tree_line_length]
            if char_at_pos == "#":
                count += 1
            index += x
    return count

product = 1

for i, nr in enumerate(x):
    print(count_trees(x[i], y[i]))
    product *= count_trees(x[i], y[i])

print(product)