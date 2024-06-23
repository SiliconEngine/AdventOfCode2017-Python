#!/usr/bin/python
"""Advent of Code 2017, Day 22, Part 1 and Part 2

https://adventofcode.com/2017/day/22

We're given a set of rules for how a virus moves around a map spreading an infection.
Part 1 calculates the number of new infections after 10,000 iterations. Part 2 uses
slightly more complex rules and 10M iterations.

This was really about the data structure, which uses a coordinate hash to keep track
of the grid.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'map.dat'

DIR_N, DIR_E, DIR_S, DIR_W = 0, 1, 2, 3
moves = ((0, -1), (1, 0), (0, 1), (-1, 0))

def part1(infected, x, y, d):
    caused_inf = 0
    for action in range(10_000):
        if (x, y) in infected:
            d = (d + 1) % 4
            del infected[(x, y)]
        else:
            d = (d - 1) % 4
            infected[(x, y)] = 'I'
            caused_inf += 1

        x, y = x+moves[d][0], y+moves[d][1]

    return caused_inf

def part2(infected, x, y, d):
    caused_inf = 0
    for action in range(10_000_000):
        state = 'C' if (x, y) not in infected else infected[(x, y)]
        if state == 'C':
            d = (d - 1) % 4             # Turn left
            infected[(x, y)] = 'W'
        elif state == 'W':
            infected[(x, y)] = 'I'
            caused_inf += 1
        elif state == 'I':
            d = (d + 1) % 4             # Turn right
            infected[(x, y)] = 'F'
        elif state == 'F':
            d = (d + 2) % 4             # Turn around
            del infected[(x, y)]

        x, y = x+moves[d][0], y+moves[d][1]

    return caused_inf

infected = { }
with open(fn, 'r') as file:
    len_y = 0
    for line in file:
        for x, c in enumerate(list(line.rstrip())):
            if c == '#':
                infected[((x, len_y))] = 'I'
        len_y += 1
        len_x = len(line)-1

print(f"Part 1: {part1(infected.copy(), len_x // 2, len_y // 2, DIR_N)}")
print(f"Part 2: {part2(infected.copy(), len_x // 2, len_y // 2, DIR_N)}")
