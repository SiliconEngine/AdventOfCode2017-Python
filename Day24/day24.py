#!/usr/bin/python
"""Advent of Code 2017, Day 24, Part 1 and Part 2

https://adventofcode.com/2017/day/24

Given a list of components with socket ends, Part 1 computes the highest "strength"
combination of components. Part 2 computes the highest strength of the longest chain
of components.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'components.dat'

from collections import defaultdict

with open(fn, 'r') as file:
    comps = [ tuple(map(int, line.rstrip().split('/'))) for line in file ]

ends = defaultdict(set)
for c in comps:
    ends[c[0]].add(c)
    ends[c[1]].add(c)

best_strength, longest, longest_strength = 0, 0, 0

# Recursively do depth-first-search on components
# Note that the list of components does not have duplicates. Things would probably
# need to be different in that case.
def find(cur_end, used=set(), chain=[]):
    global best_strength, longest, longest_strength
    for c in ends[cur_end]:
        if c not in used:
            other_end = c[1] if c[0] == cur_end else c[0]
            used.add(c)
            chain.append(c)

            length, strength = len(chain), sum(c[0]+c[1] for c in chain)
            if strength > best_strength:
                best_strength = strength
            if length == longest and strength > longest_strength:
                longest_strength = strength
            if length > longest:
                longest = length
                longest_strength = strength

            find(other_end, used, chain)
            used.remove(c)
            chain.pop()

find(0)
print(f"Part 1: Best strength: {best_strength}")
print(f"Part 2: Longest is {longest}, best strength is {longest_strength}")
