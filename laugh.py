#!/usr/bin/python3

from sys import argv
from random import randint

if len(argv) == 1:
    print("need len")
    exit(1)

count = int(argv[1])

str = ""
for _ in range(count):
    str += chr(randint(65, 90))

print(str)

