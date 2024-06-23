#!/usr/bin/python
"""Advent of Code 2017, Day 5, Part 1 and Part 2

https://adventofcode.com/2017/day/5

Given a list of "jump offsets", follow the chain until it's outside the offset list. For Part 1,
the offset is incremented by one after each jump. For Part 2, the offset is either incremented
or decremented, depending on the value.

See offsets.dat for full data.

Author: Tim Behrendsen
"""

fn = 'offsets.dat'

def calc(offsets, rule):
    work = offsets.copy()
    idx, step = 0, 0
    while idx >= 0 and idx < len(work):
        jump = work[idx]
        work[idx] += rule(jump)
        idx += jump
        step += 1

    return step

# Read in offset list
with open(fn, 'r') as file:
    offsets = [ int(s.rstrip('\n')) for s in file ]

print(f"Part 1 is {calc(offsets, lambda n: 1)}")
print(f"Part 2 is {calc(offsets, lambda n: 1 if n < 3 else -1)}")
