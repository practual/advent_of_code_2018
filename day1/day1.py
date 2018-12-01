#! /usr/bin/env python

# http://adventofcode.com/2018/day/1

import sys

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

freq_changes = list(map(int, puzzle_input.strip().split('\n')))

print(sum(freq_changes))

seen_freqs = {}
current_freq = 0
i = 0
freq_index = 0
while True:
    if current_freq in seen_freqs:
        break
    seen_freqs[current_freq] = True
    try:
        current_freq += freq_changes[freq_index]
    except IndexError:
        freq_index = 0
        current_freq += freq_changes[freq_index]
    freq_index += 1
    i += 1

print('Seen frequency {} twice after inspecting {} frequency changes.'.format(current_freq, i))
