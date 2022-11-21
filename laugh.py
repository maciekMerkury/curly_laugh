#!/usr/bin/python3

from sys import argv
from random import randint

LEFT = {
    'S': 100,
    'D': 50,
    'F': 50,
}

RIGHT = {
    'K': 100,
}

l_w = sum([LEFT[k] for k in LEFT])
r_w = sum([RIGHT[k] for k in RIGHT])

def int_to_w_char(i: int, r: bool) -> chr:
    map = RIGHT if r else LEFT
    for k in map:
        if i <= map[k]:
            return k
        else:
            i -= map[k]

    print("how")
    exit(2)


if len(argv) == 1:
    print("need len")
    exit(1)

count = int(argv[1])

str = ""
for i in range(count):
    # i % 2 == 0 starts from 0, thus the first char is from the right, per spec
    right = i % 2 == 0
    w = r_w if right else l_w

    str += int_to_w_char(randint(0, w), right)

print(str)

