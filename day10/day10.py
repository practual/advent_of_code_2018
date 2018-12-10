#! /usr/bin/env python

# http://adventofcode.com/2018/day/10

import re
import sys

import numpy as np

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

params_text = puzzle_input.strip().split('\n')

pattern = re.compile('.*<(?P<px>[^,]+),(?P<py>[^>]+)>.*<(?P<vx>[^,]+),(?P<vy>[^>]+)>')

params = []
for param_text in params_text:
    match = pattern.match(param_text)
    px = int(match.group('px').strip())
    py = int(match.group('py').strip())
    params.append({
        'px': px,
        'py': py,
        'vx': int(match.group('vx').strip()),
        'vy': int(match.group('vy').strip()),
    })

# Let's make an assumption that the text will be visible when the vertical height of all the
# particles are at a minimum.
prev_y_range = float('inf')
time = 0
while True:
    range_x = [float('inf'), -float('inf')]
    range_y = [float('inf'), -float('inf')]
    for param in params:
        param['px'] += param['vx']
        param['py'] += param['vy']
        range_x = [min(range_x[0], param['px']), max(range_x[1], param['px'])]
        range_y = [min(range_y[0], param['py']), max(range_y[1], param['py'])]
    new_y_range = range_y[1] - range_y[0]
    if new_y_range > prev_y_range:
        # wind back
        range_x = [float('inf'), -float('inf')]
        range_y = [float('inf'), -float('inf')]
        for param in params:
            param['px'] -= param['vx']
            param['py'] -= param['vy']
            range_x = [min(range_x[0], param['px']), max(range_x[1], param['px'])]
            range_y = [min(range_y[0], param['py']), max(range_y[1], param['py'])]
        break
    prev_y_range = new_y_range
    time += 1

offset_x = range_x[0]
offset_y = range_y[0]
light_map = np.zeros((range_y[1] - range_y[0] + 1, range_x[1] - range_x[0] + 1), dtype=bool)
for param in params:
    light_map[param['py'] - offset_y][param['px'] - offset_x] = True

for row in light_map:
    print(''.join(map(lambda x: '#' if x else '.', row)))

print(time)
