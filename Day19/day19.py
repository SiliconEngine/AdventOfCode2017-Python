#!/usr/bin/python
"""Advent of Code 2017, Day 19, Part 1 and Part 2

https://adventofcode.com/2017/day/19

Follow an ascii-based tube and accumulate the letters along the way. Part 1 displays the
letters, and Part 2 display the total path length.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

fn = 'tubes.dat'

with open(fn, 'r') as file:
    grid = [ line.rstrip('\n') for line in file ]

dirs = { 'N': (0, -1, 'S'), 'S': (0, 1, 'N'), 'E': (1, 0, 'W'), 'W': (-1, 0, 'E') }
x, y = grid[0].index('|'), 0
cur_d, letters, count = 'S', [], 0
valid_turns = lambda cur_d: [d for d in dirs if d != dirs[cur_d][2] and grid[y + dirs[d][1]][x + dirs[d][0]] != ' ']

while True:
    count += 1
    c = grid[y][x]
    if c.isalpha():
        letters.append(c)
        if len(valid_turns(cur_d)) == 0:
            break
    elif c == '+':
        cur_d = valid_turns(cur_d)[0]
    x, y = x+dirs[cur_d][0], y+dirs[cur_d][1]

print(f"Part 1: {''.join(letters)}")
print(f"Part 2: {count}")
