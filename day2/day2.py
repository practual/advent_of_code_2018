#! /usr/bin/env python

# http://adventofcode.com/2018/day/2

import sys
from collections import Counter

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

box_ids = puzzle_input.strip().split('\n')

twos_count = 0
threes_count = 0
for box_id in box_ids:
    letter_counts = set(Counter(box_id).values())
    twos_count += 2 in letter_counts
    threes_count += 3 in letter_counts

print(twos_count * threes_count)

ID_LEN = 26
masked_ids = {}
found_mask = None
for box_id in box_ids:
    for i in range(ID_LEN):
        mask = box_id[:i] + '-' + box_id[i+1:]
        if mask in masked_ids:
            found_mask = mask
            break
        masked_ids[mask] = True
    if found_mask:
        break

print(found_mask)
