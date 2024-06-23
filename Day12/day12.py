#!/usr/bin/python
"""Advent of Code 2017, Day 12, Part 1 and Part 2

https://adventofcode.com/2017/day/12

We're given a tree of "pipes". Part 1 calculates the number of unique pipes connected
to pipe #0. Part 2 calculates the number of unique unrelated groups to don't connect
to each other.

See pipes.dat for full data.

Author: Tim Behrendsen
"""

fn = 'pipes.dat'

import re

# Recursively follow pipes and mark visited ones in the set
def scan(pipe_set, pipe):
    pipe_set.add(pipe)
    for p in pipes[pipe]:
        if p not in pipe_set:
            scan(pipe_set, p)

# Calculate how many pipes connect to #0
def part1(pipes):
    pipe_set = set()
    scan(pipe_set, 0)
    return len(pipe_set)

# Calculate how many total unrelated groups
def part2(pipes):
    pipe_set = set()
    groups = 0
    for pipe_num in range(0, len(pipes)):
        if pipe_num not in pipe_set:
            groups += 1
            scan(pipe_set, pipe_num)

    return groups

pipes = []
with open(fn, 'r') as file:
    for line in file:
        m = re.findall('\d+', line)
        pipes.append(list(map(int, m[1:])))

print(f"Part 1 is {part1(pipes)}")
print(f"Part 2 is {part2(pipes)}")
