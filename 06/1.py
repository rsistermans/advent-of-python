import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(CURR_DIR, "input.txt"), "r")
lines = file.read().splitlines()

groups = [""]

for line in lines:
    if(line == ""):
        groups.append("")
    else:
        groups[-1] = "".join(set(groups[-1] + line))

answer_count = 0
for group in groups:
    answer_count = answer_count + len(group)

print(answer_count)