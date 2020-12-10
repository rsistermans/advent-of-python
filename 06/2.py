import os

def get_answers(group):
    answers = dict.fromkeys({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}, 0)
    for person in group:
        for answer in person:
            count = answers.get(answer)
            answers[answer] = count + 1
    unanimous_answers = dict()
    for(key, value) in answers.items():
        if value == len(group):
            unanimous_answers[key] = value
    return len(unanimous_answers)

# on to the program

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(CURR_DIR, "input.txt"), "r")
lines = file.read().splitlines()

groups = [[]]

for line in lines:
    if(line == ""):
        groups.append([])
    else:
        groups[-1].append(line)

count = 0

for group in groups:
    count = count + get_answers(group)

print(count)
