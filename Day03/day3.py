#!/usr/bin/python
"""Advent of Code 2017, Day 3, Part 1 and Part 2

https://adventofcode.com/2017/day/3

Given a path through squares that are a spiral, part 1 calculates the distance at
a certain number of squares. For part 2, each square contains the sum of the values
of the surrounding squares, and we need to find the first total that exceeds the
target number.

Author: Tim Behrendsen
"""

target = 361527

# Iterator to generate spiral coordinates
def spiral():
    radius, last_x, last_y = 0, (0, 0), (0, 0)
    while True:
        radius += 1
        x1, x2 = -radius, radius
        y1, y2 = -radius, radius
        start = (last_x[1]+1, last_y[1])
        for y in range(start[1], y1, -1):
            yield (start[0], y)
        for x in range(x2, x1-1, -1):
            yield (x, y1)
        for y in range(y1+1, y2+1):
            yield (x1, y)
        for x in range(x1+1, x2+1):
            yield (x, y2)

        last_x, last_y = (x1, x2), (y1, y2)

# Part 1: Figure out coordinates of target value
def part1():
    n = 1
    for x, y in spiral():
        n += 1
        if n == target:
            return x, y, n

# Part 2: Each grid location is the sum of the surrounding grid locations
def part2():
    grid = { (0, 0): 1 }

    def set(x, y):
        total = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx != 0 or dy != 0) and (x+dx, y+dy) in grid:
                    total += grid[(x+dx, y+dy)]

        grid[(x, y)] = total
        return total

    for x, y in spiral():
        total = set(x, y)
        if total > target:
            return x, y, total

x, y, n = part1()
print(f"Answer: {(x, y)} = {n}, dist = {abs(x) + abs(y)}")

x, y, total = part2()
print(f"Answer: {(x, y)} = {total}")
