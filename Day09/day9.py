#!/usr/bin/python
"""Advent of Code 2017, Day 9, Part 1 and Part 2

https://adventofcode.com/2017/day/9

Given a stream of characters, parse and identify "garbage" based on given rules.
Part 1 counts the number of "groups". Part 2 counts the number of characters
identified has garbage.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

fn = 'stream.dat'

NORMAL = 1
GARBAGE = 2

with open(fn, 'r') as file:
    line = file.readline().rstrip('\n')

group_count, score, bad_count = 0, 0, 0
state, level, idx = NORMAL, 0, 0
while idx < len(line):
    c = line[idx]
    if c == '!':            # Skip next character
        idx += 1

    elif state == NORMAL:
        if c == '{':
            level += 1
        elif c == '}':
            group_count += 1
            score += level
            level -= 1
        elif c == '<':      # Start of garbage
            state = GARBAGE
        elif c == ',':      # Isn't strictly necessary to look at commas
            pass

    elif state == GARBAGE:
        if c == '>':
            state = NORMAL
        else:
            bad_count += 1

    idx += 1

print(f"Part 1 is {score}")
print(f"Part 2 is {bad_count}")
