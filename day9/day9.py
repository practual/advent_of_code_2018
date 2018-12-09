#! /usr/bin/env python

# http://adventofcode.com/2018/day/9

from collections import defaultdict, deque


def find_high_score(num_players, max_marble_value):
    marbles = deque([0])
    player_points = defaultdict(int)

    current_player = 1
    for marble in range(1, max_marble_value + 1):
        if marble % 23:
            marbles.rotate(-1)
            marbles.append(marble)
        else:
            marbles.rotate(7)
            player_points[current_player] += marble + marbles.pop()
            marbles.rotate(-1)
        current_player += 1
        current_player %= num_players

    return max(player_points.values())


print(find_high_score(476, 71431))
print(find_high_score(476, 7143100))
