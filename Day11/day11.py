#!/usr/bin/python
"""Advent of Code 2017, Day 11, Part 1 and Part 2

https://adventofcode.com/2017/day/11

Given a hexagonal grid and a list of moves, Part 1 calculates the number of steps it ends up
from the original. In Part 2 calculates the furthest it ever was during the travel.

See test.dat for test data and counts.dat for full data.

GRID METHOD:
0,0   2,0   4,0
   1,1   3,1   5,1
0,2   2,2   4,2
   1,3   3,3   5,3

Author: Tim Behrendsen
"""

fn = 'path.dat'
dirs = { 'n': (0, -2), 's': (0, 2), 'nw': (-1, -1), 'sw': (-1, 1), 'ne': (1, -1), 'se': (1, 1) }

def move(x, y, d):
    delta = dirs[d]
    return x + delta[0], y + delta[1]

# Wind backward from coordinates to figure out number of steps to 0, 0.
# There's probably a clever way to calculate this, but I wasn't confident in
# calculating a distance using hex coordinates.
def calc_steps(x, y):
    steps = 0
    while (x, y) != (0, 0):
        if x == 0:
            d = 'n' if y > 0 else 's'
        elif x < 0:
            d = 'ne' if y > 0 else 'se'
        else:
            d = 'nw' if y > 0 else 'sw'
        x, y = move(x, y, d)
        steps += 1

    return steps

with open(fn, 'r') as file:
    moves = file.readline().rstrip('\n').split(',')

# Follow given path to final coordinates
x, y = 0, 0
most = 0
for d in moves:
    x, y = move(x, y, d)
    most = max(most, calc_steps(x, y))

# Calculate number of steps from final spot to origin
print(f"Part 1 is {calc_steps(x, y)} steps")

# Display furthest away ever during path
print(f"Part 2 is {most} steps")
