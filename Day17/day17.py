#!/usr/bin/python
"""Advent of Code 2017, Day 17, Part 1 and Part 2

https://adventofcode.com/2017/day/17

Process insertions into a buffer using a certain pattern. For Part 1, it displays
the value after '2017', with 2017 iterations. For Part 2, it has to simulate
50M iterations and display the number after 0, and so it needed a shortcut.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

steps = 3               # Test number
steps = 324

# Part 1 just uses the naive algorithm, too slow for Part 2
def part1():
    buffer, pos = [ 0 ], 0
    for i in range(2017):
        pos = (pos + steps) % len(buffer) + 1
        buffer.insert(pos, i+1)

    return buffer[(buffer.index(2017)+1) % len(buffer)]

# For Part 2, we note that the position of zero never changes from position 0, so
# we just have to track when something is inserted at position 1.
def part2():
    pos, final_value = 0, 0
    for i in range(1, 50_000_001):
        if (pos := (pos + steps) % i + 1) == 1:
            final_value = i

    return final_value

print(f"Part 1 is {part1()}")
print(f"Part 2 is {part2()}")
