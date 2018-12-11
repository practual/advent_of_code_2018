#! /usr/bin/env python

# http://adventofcode.com/2018/day/11

import numpy as np


def get_power_level(y, x):
    rack_id = x + 10
    power_level = (rack_id * y + 1133) * rack_id
    hundreds_digit = power_level // 100 % 10
    return hundreds_digit - 5


cells = np.fromfunction(get_power_level, (300, 300), dtype=int)

max_sum = -float('inf')
max_sum_coords = (0, 0)
max_sum_size = 0
for square_size in range(1, 300 + 1):
    max_sum_for_size_coords = (0, 0)
    max_sum_for_size = -float('inf')
    for y in range(cells.shape[0]):
        if y + square_size >= cells.shape[0]:
            break
        for x in range(cells.shape[1]):
            if x + square_size >= cells.shape[1]:
                continue
            grid_sum = np.sum(cells[y:y+square_size, x:x+square_size])
            if grid_sum > max_sum_for_size:
                max_sum_for_size = grid_sum
                max_sum_for_size_coords = (x, y)
            if grid_sum > max_sum:
                max_sum = grid_sum
                max_sum_coords = (x, y)
                max_sum_size = square_size

    print('MAX FOR SIZE', square_size, max_sum_for_size_coords)

print('TOTAL MAX', max_sum_size, max_sum_coords)
