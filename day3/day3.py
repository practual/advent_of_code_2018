#! /usr/bin/env python

# http://adventofcode.com/2018/day/3

import sys

import numpy as np

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

areas = puzzle_input.strip().split('\n')

area_arrays = {}

num_overlaps = 0
overlap_array = np.zeros((1000, 1000), dtype=int)
for area in areas:
    area_id, _, coords, size = area.split()
    x, y = map(int, coords.strip(':').split(','))
    w, h = map(int, size.split('x'))

    area_array = np.zeros((1000, 1000), dtype=int)
    area_array[y:y + h, x:x + w] = 1
    area_arrays[area_id] = area_array

    overlap_array += area_array

overlap_mask = overlap_array > 1

print('Number of overlapping squares', np.sum(overlap_mask))

for area_id, area_array in area_arrays.items():
    if not np.any(area_array * overlap_mask):
        print('Non overlapping ID', area_id)
        break
