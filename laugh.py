#!/usr/bin/python3

from sys import argv
from random import randint

VALID_LETTERS = {
    'S': 100,
    'K': 100,
    'D': 50,
    'F': 50,
}

total_w = sum([VALID_LETTERS[k] for k in VALID_LETTERS])

def int_to_weighted_char(i: int) -> chr:
    for k in VALID_LETTERS:
        if i <= VALID_LETTERS[k]:
            return k
        else:
            i -= VALID_LETTERS[k]

    print("how")
    exit(1)


if len(argv) == 1:
    print("need len")
    exit(1)

count = int(argv[1])

str = ""
for _ in range(count):
    str += int_to_weighted_char(randint(0, total_w))

print(str)

