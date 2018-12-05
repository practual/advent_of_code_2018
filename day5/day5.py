#! /usr/bin/env python

# http://adventofcode.com/2018/day/5

import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

polymer_string = puzzle_input.strip()


def get_opposite(char):
    if ord(char) >= 97:
        # Lowercase
        return char.upper()
    return char.lower()


def react(polymer, exclude_char=None):
    stack = []
    for unit in polymer:
        if unit == exclude_char or get_opposite(unit) == exclude_char:
            continue
        if len(stack) and stack[-1] == get_opposite(unit):
            stack.pop()
        else:
            stack.append(unit)
    return stack


print(len(react(polymer_string)))

trials = []
for c in range(65, 65 + 26):
    trials.append(len(react(polymer_string, chr(c))))

print(min(trials))
