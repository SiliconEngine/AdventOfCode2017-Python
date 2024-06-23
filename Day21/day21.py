#!/usr/bin/python
"""Advent of Code 2017, Day 21, Part 1 and Part 2

https://adventofcode.com/2017/day/21

Given a list of transformation rules for a 2D grid pattern, apply them according to
the puzzle rules. For part 1, do five transformations, and 18 for part 2.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'test.dat'
fn = 'rules.dat'

rotate_list = lambda matrix: tuple(zip(*matrix[::-1]))
invert_h = lambda matrix: tuple(tuple(reversed(row)) for row in matrix)
invert_v = lambda matrix: tuple(tuple(row) for row in matrix[::-1])

# Create dict of rules, along with each variant
rules = { }
with open(fn, 'r') as file:
    for line in file:
        inp, out = line.rstrip().split(' => ')
        inp_list = tuple(tuple(s) for s in inp.split('/'))
        out_list = [ list(s) for s in out.split('/') ]
        r = inp_list
        for i in range(4):
            rules[r] = out_list
            rules[invert_v(r)] = out_list
            rules[invert_h(r)] = out_list
            r = rotate_list(r)

pattern = [ list('.#.'), list('..#'), list('###') ]
for count in range(18):
    size = len(pattern[0])
    reg_size_o, reg_size_n = (2, 3) if (size % 2) == 0 else (3, 4)
    new_size = (size // reg_size_o) * reg_size_n
    new_pattern = [ [] for _ in range(new_size) ]
    # Split off each region and apply the rule, adding to new_pattern
    for reg_y in range(size // reg_size_o):
        for reg_x in range(size // reg_size_o):
            src_x, src_y = reg_x * reg_size_o, reg_y * reg_size_o
            region = tuple(tuple(p[src_x:src_x+reg_size_o]) for p in pattern[src_y:src_y+reg_size_o])
            dest_y, r = reg_y * reg_size_n, rules[region]
            for i in range(reg_size_n):
                new_pattern[dest_y+i] += r[i]

    pattern = new_pattern
    if count == 4:
        part1 = sum(c == '#' for p in pattern for c in p)

print(f"Part 1: {part1}")
print(f"Part 2: {sum(c == '#' for p in pattern for c in p)}")
