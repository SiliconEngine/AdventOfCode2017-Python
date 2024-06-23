#!/usr/bin/python
"""Advent of Code 2017, Day 16, Part 1 and Part 2

https://adventofcode.com/2017/day/16

Starting with a sequence of letters, perform "dance moves" to cycle the letters.
Part 1 executes the pattern once. Part 2 predicts the pattern after 1 billion moves.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'dance.dat'

def dance(line):
    for op, p1, p2 in moves:
        if op == 's':                   # Spin
            for i in range(int(p1)):
                line.insert(0, line.pop())
        elif op == 'x':                 # Exchange
            line[int(p1)], line[int(p2)] = line[int(p2)], line[int(p1)]
        elif op == 'p':                 # Partner
            i1, i2 = line.index(p1), line.index(p2)
            line[i1], line[i2] = p2, p1
    return line

with open(fn, 'r') as file:
    moves = [ re.findall('(.)(\w+)/?(\w*)?', s)[0] for s in file.readline().rstrip('\n').split(',') ]

# Part 1: Figure out pattern after one dance
# Part 2: Figure out when sequence repeats, then extrapolate to full number
line = [ chr(i+ord('a')) for i in range(16) ]
seq = [ ''.join(line) ]
while (k := ''.join(dance(line))) != seq[0]:
    seq.append(k)

print(f"Part 1: {seq[1]}")
print(f"Part 2: {seq[1_000_000_000 % len(seq)]}")
