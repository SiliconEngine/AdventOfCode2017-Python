#!/usr/bin/python
"""Advent of Code 2017, Day 6, Part 1 and Part 2

https://adventofcode.com/2017/day/6

Given a set of "block counts", figure out which block has the highest count,
then redistribute that count to the other blocks. For Part 1, figure out when
the cycle repeats to any prior state. For Part 2, continue after that and see
when that repeated one repeats again.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'counts.dat'

def find_cycle(counts, part):
    banks = counts.copy()
    num_banks = len(banks)
    dup_chk = set()
    count, state = 0, 0

    while True:
        count += 1

        # Find bank with highest number, ties are lowest index first
        highest, most_idx = max([ (banks[i], -i) for i in range(num_banks) ])

        # Redistribute highest among other banks
        idx = 0-most_idx
        banks[idx] = 0
        while highest:
            idx = (idx+1) % num_banks
            banks[idx] += 1
            highest -= 1

        # Check if we've seen this pattern before
        chk = tuple(banks)
        if chk in dup_chk:
            if part == 1 or state == 1:
                break

            # Part 2 continues until we get a repeat of this same base
            state = 1           # Mark that we've done the first cycle and reset
            count = 0
            dup_chk = set()

        dup_chk.add(chk)

    return count

# Read in number list
with open(fn, 'r') as file:
    counts = [ int(n) for n in re.findall('\d+', file.readline()) ]

print(f"Part 1 is {find_cycle(counts, part=1)}")
print(f"Part 2 is {find_cycle(counts, part=2)}")
