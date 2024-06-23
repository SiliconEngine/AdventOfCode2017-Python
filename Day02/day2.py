#!/usr/bin/python
"""Advent of Code 2017, Day 2, Part 1 and Part 2

https://adventofcode.com/2017/day/2

Given a spreadsheet of numbers, first calculate the sum of the differences
of the highest and lowest numbers for each row. For part 2, figure out which
pair in each row are evenly divisible and total up those quotients.

See ss.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'ss.dat'

def part1(ss):
    return sum(max(r) - min(r) for r in ss)

def part2(ss):
    def find(r):
        for i1 in range(len(r)):
            for i2 in range(i1+1, len(r)):
                if (r[i1] % r[i2]) == 0:
                    return r[i1] // r[i2]
                if (r[i2] % r[i1]) == 0:
                    return r[i2] // r[i1]
    return sum(find(r) for r in ss)

# Read in number list
ss = [ ]
with open(fn, 'r') as file:
    for line in file:
        ss.append([ int(n) for n in re.findall('\d+', line) ])

print(f"Part 1 is {part1(ss)}")
print(f"Part 2 is {part2(ss)}")
