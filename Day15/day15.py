#!/usr/bin/python
"""Advent of Code 2017, Day 15, Part 1 and Part 2

https://adventofcode.com/2017/day/15

Given two number generators, count the number of times the lower 16 bits
match. Part 1 and Part 2 has some variations in how the numbers are generated.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'gen.dat'

# Generate values 
def gen(val, factor, div):
    while True:
        val = val * factor % 2147483647
        if val % div == 0:
            yield val

# Part 1, part 2 using a yield generator
def calc(val_a, val_b, max_count, div_a, div_b):
    gen_a, gen_b = gen(val_a, 16807, div_a), gen(val_b, 48271, div_b)
    return sum(next(gen_a) & 0xffff == next(gen_b) & 0xffff for i in range(max_count))

with open(fn, 'r') as file:
    val_a, val_b = [ int(re.findall('\d+', line)[0]) for line in file ]

print(f"Part 1 is {calc(val_a, val_b, 40_000_000, 1, 1)}")
print(f"Part 2 is {calc(val_a, val_b, 5_000_000, 4, 8)}")
