#! /usr/bin/env python

# http://adventofcode.com/2018/day/5

import sys

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
        if exclude_char in [unit, get_opposite(unit)]:
            continue
        if len(stack) and stack[-1] == get_opposite(unit):
            stack.pop()
        else:
            stack.append(unit)
    return stack


print(len(react(polymer_string)))

trials = [len(react(polymer_string, chr(c))) for c in range(65, 65 + 26)]

print(min(trials))
