#! /usr/bin/env python

# http://adventofcode.com/2018/day/6

import sys
from collections import Counter

import numpy as np

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

coordinates_text = puzzle_input.strip().split('\n')

coordinates = []
min_x = float('inf')
max_x = 0
min_y = float('inf')
max_y = 0
for coordinate_text in coordinates_text:
    x, y = map(int, coordinate_text.split(', '))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    coordinates.append((x, y))

# Don't make the area any bigger than necessary...
coordinates = [(x - min_x, y - min_y) for x, y in coordinates]
max_x -= min_x
max_y -= min_y


def get_distance_function(coord):
    def get_distance(x, y):
        return abs(x - coord[0]) + abs(y - coord[1])
    return get_distance


distance_map = np.zeros((max_x, max_y), dtype=(int, 2))
min_distances = np.full((max_x, max_y), np.inf)
total_distances = np.zeros((max_x, max_y), dtype=int)

for coordinate in coordinates:
    # Make an array of distances from the coordinate.
    distances = np.fromfunction(get_distance_function(coordinate), (max_x, max_y), dtype=int)
    # Find where these distances are a new minimum distance to any coordinate.
    new_min_locations = (distances < min_distances).nonzero()
    # Update our labeled array to show which coordinate is the minimum distance at that location.
    distance_map[new_min_locations] = coordinate
    # Any location which is equally distant to an existing coordinate gets marked with the fake
    # coordinate (-1, -1).
    distance_map[(distances == min_distances).nonzero()] = (-1, -1)
    # Update our record of the minimum distances.
    min_distances[new_min_locations] = distances[new_min_locations]
    total_distances += distances


# PART 1
# Assume that any areas from around the edge of the map would go on to infinity.
infinite_areas = set()
infinite_areas.update(tuple(map(tuple, distance_map[0,:])))
infinite_areas.update(tuple(map(tuple, distance_map[max_x-1,:])))
infinite_areas.update(tuple(map(tuple, distance_map[:,0])))
infinite_areas.update(tuple(map(tuple, distance_map[:,max_y-1])))
# Add (-1, -1) as a quick way to make this an invalid answer.
infinite_areas.add((-1, -1))

# Don't need a 2D map anymore, so just flatten it (well, to a list of tuples).
flat_map = distance_map.reshape(max_x * max_y, 2)

# Count size of areas, and find the top X occurrences, where X is larger than the number of infinite
# areas to guarantee we find a non-infinite area.
# Then just get the first value that isn't infinite.
print(next(area[1] for area in Counter(map(tuple, flat_map)).most_common(len(infinite_areas) + 1) if area[0] not in infinite_areas))

# PART 2
# This probably wouldn't work in the general case as there could be suitable locations outside of the
# trimmed area that we've defined. e.g. if you only have 1 coordinate, the area would be 1x1, and
# we wouldn't be checking all the locations around it.
# Could make this work for the general case by padding the area by 10000 on each side, but luckily
# we didn't need to for our input, as this yields the correct answer.
print(np.sum(total_distances < 10000))
