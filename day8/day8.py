#! /usr/bin/env python

# http://adventofcode.com/2018/day/8

import sys

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

license_list = list(map(int, puzzle_input.strip().split()))

global_meta_sum = 0


def process_node(start):
    global global_meta_sum

    num_children = license_list[start]
    num_meta = license_list[start + 1]

    child_values = []
    meta_start = start + 2
    while num_children:
        child_value, meta_start = process_node(meta_start)
        child_values.append(child_value)
        num_children -= 1

    meta_end = meta_start + num_meta
    meta = license_list[meta_start:meta_end]
    meta_sum = sum(meta)

    global_meta_sum += meta_sum

    if not child_values:
        return meta_sum, meta_end

    node_value = 0
    for child_index in meta:
        try:
            node_value += child_values[child_index - 1]
        except IndexError:
            pass

    return node_value, meta_end


root_value, _ = process_node(0)

print(global_meta_sum, root_value)
