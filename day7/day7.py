#! /usr/bin/env python

# http://adventofcode.com/2018/day/7

import re
import sys
from collections import defaultdict

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

rules_text = puzzle_input.strip().split('\n')


def make_blank_rule():
    return {
        'preceding': [],
        'following': [],
    }


rules = defaultdict(make_blank_rule)
pattern = re.compile('Step ([A-Z]).*([A-Z])')
for rule_text in rules_text:
    match = re.match(pattern, rule_text)
    preceding = match.group(1)
    following = match.group(2)
    rules[preceding]['following'].append(following)
    rules[following]['preceding'].append(preceding)

done_rules = []


def get_viable_rules(candidates):
    viables = []
    for candidate in candidates:
        if all(rule in done_rules for rule in rules[candidate]['preceding']):
            viables.append(candidate)
    return viables


viable_rules = sorted(get_viable_rules(rules.keys()), reverse=True)

while len(done_rules) < len(rules):
    rule = viable_rules.pop()
    done_rules.append(rule)
    viable_rules += get_viable_rules(rules[rule]['following'])
    viable_rules = sorted(viable_rules, reverse=True)

print(''.join(done_rules))

done_rules = []
active_rules = {}
workers = 5
second = -1
viable_rules = get_viable_rules(rules.keys())

while len(done_rules) < len(rules):
    second += 1
    # Copy the active rules so we can delete entries mid-loop.
    for active_rule, time_finished in [(r, t) for r, t in active_rules.items()]:
        if second == time_finished:
            done_rules.append(active_rule)
            viable_rules += get_viable_rules(rules[active_rule]['following'])
            del active_rules[active_rule]
            workers += 1

    if not workers or not viable_rules:
        continue

    viable_rules = sorted(viable_rules, reverse=True)
    while workers and viable_rules:
        rule = viable_rules.pop()
        time_for_rule = ord(rule) - 65 + 1 + 60
        active_rules[rule] = second + time_for_rule
        workers -= 1

print(''.join(done_rules))
print(second)
