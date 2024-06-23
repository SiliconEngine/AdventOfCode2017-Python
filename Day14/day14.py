#!/usr/bin/python
"""Advent of Code 2017, Day 14, Part 1 and Part 2

https://adventofcode.com/2017/day/14

Using the "knot hash" algorithm from Day 10, create a grid of 0s and 1. Part 1
computes the total number of 1s. Part 2 computes the total number of contiguous
regions.

Author: Tim Behrendsen
"""

from functools import reduce

key = 'flqrgnkx'    # Test
key = 'ffayrhll'

# "Knot hash" algorithm from Day 10
def hash(s, num_rounds=64, buffer_len=256):
    lengths = [ ord(c) for c in s ] + [ 17, 31, 73, 47, 23 ]
    buffer = list(range(buffer_len))
    pos, skip = 0, 0
    for round in range(num_rounds):
        for l in lengths:
            # Reverse elements
            pos1 = pos
            pos2 = (pos + l - 1) % buffer_len
            for i in range(l // 2):
                buffer[pos1], buffer[pos2] = buffer[pos2], buffer[pos1]
                pos1 = (pos1+1) % buffer_len
                pos2 = (pos2-1) % buffer_len

            pos = (pos + l + skip) % buffer_len
            skip += 1

    output = [ reduce(lambda x, y: x ^ y, buffer[i:i+16]) for i in range(0, buffer_len, 16) ]
    return ''.join((('%02x' % n) for n in output))

# Part 1: Calculate total number of "filled" spaces
def part1(grid):
    return sum(len([c for c in grid[i] if c == '1']) for i in range(128))

# Part 1: Calculate total number of contiguous regions
def part2(grid):
    seen = set()

    # Recursively find all adjacent squares and mark them seen
    def find(row, col):
        seen.add((row, col))
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r2, c2 = row+dr, col+dc
            if 0 <= r2 < 128 and 0 <= c2 < 128 and grid[r2][c2] == '1' and (r2, c2) not in seen:
                find(r2, c2)

    # Count number of regions. Each time we find a space we haven't seen before,
    # it's a new region, and then we mark the contiguous area.
    count = 0
    for row in range(128):
        for col in range(128):
            if grid[row][col] == '1' and (row, col) not in seen:
                count += 1
                find(row, col)

    return count

hextobin = { hex(i)[2:]: bin(i)[2:].zfill(4) for i in range(16) }
grid = [ ''.join((hextobin[c] for c in hash(f"{key}-{i}"))) for i in range(128) ]
print(f"Part 1 is {part1(grid)}")
print(f"Part 2 is {part2(grid)}")

