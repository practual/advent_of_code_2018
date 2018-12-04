#! /usr/bin/env python

# http://adventofcode.com/2018/day/4

import re
import sys
from collections import Counter, defaultdict
from datetime import datetime

input_file_name = sys.argv[1]

with open(input_file_name, 'r') as file:
    puzzle_input = file.read()

events_text = puzzle_input.strip().split('\n')

pattern = re.compile('\[(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})\] (Guard #(?P<id>[0-9]+)|(?P<start>falls)|(?P<end>wakes))')

events = []
for event_text in events_text:
    match = pattern.match(event_text)
    events.append({
        'time': datetime.strptime(match.group('date'), '%Y-%m-%d %H:%M'),
        'id': match.group('id'),
        'start': match.group('start'),
        'end': match.group('end'),
    })

sorted_events = sorted(events, key=lambda x: x['time'])

guard_counters = defaultdict(Counter)
for event in sorted_events:
    if event['id']:
        guard_id = int(event['id'])
    if event['start']:
        start_time = event['time'].minute
    if event['end']:
        end_time = event['time'].minute
        guard_counters[guard_id].update(range(start_time, end_time))

sleepiest_guard = max(guard_counters.items(), key=lambda g: sum(g[1].values()))

print(sleepiest_guard[0] * sleepiest_guard[1].most_common(1)[0][0])

most_consistent_guard = max(guard_counters.items(), key=lambda g: g[1].most_common(1)[0][1])

print(most_consistent_guard[0] * most_consistent_guard[1].most_common(1)[0][0])
