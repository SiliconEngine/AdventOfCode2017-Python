#!/usr/bin/python
"""Advent of Code 2017, Day 10, Part 1 and Part 2

https://adventofcode.com/2017/day/10

Implement an unusual hashing function.

See lengths.dat for full data.

Author: Tim Behrendsen
"""

from functools import reduce

fn = 'lengths.dat'
list_size = 256

def hash(lengths, num_rounds):
    buffer = list(range(list_size))
    pos, skip = 0, 0
    for round in range(num_rounds):
        for l in lengths:
            # Reverse elements
            pos1 = pos
            pos2 = (pos + l - 1) % list_size
            for i in range(l // 2):
                buffer[pos1], buffer[pos2] = buffer[pos2], buffer[pos1]
                pos1 = (pos1+1) % list_size
                pos2 = (pos2-1) % list_size

            pos = (pos + l + skip) % list_size
            skip += 1

    return buffer

with open(fn, 'r') as file:
    line = file.readline().rstrip('\n')

lengths = [ int(n) for n in line.split(',') ]
buffer = hash(lengths, 1)
print(f"Part 1 is {buffer[0] * buffer[1]}")

lengths = [ ord(c) for c in line ] + [ 17, 31, 73, 47, 23 ]
buffer = hash(lengths, 64)
output = [ reduce(lambda x, y: x ^ y, buffer[i:i+16]) for i in range(0, 256, 16) ]
print(f"Part 2 is {''.join([ ('%02x' % n) for n in output ])}")
