#!/usr/bin/python
"""Advent of Code 2017, Day 1, Part 1 and Part 2

https://adventofcode.com/2017/day/1

Given a list of digits, calculate the sum of digits that have the same digit at an
offset (wrapping around the end). Part 1, offset is 1. For part 2, offset is half
the length.

See captcha.dat for full data.

Author: Tim Behrendsen
"""

fn = 'captcha.dat'

def compute(num_list, offset):
    n = 0
    for i in range(len(num_list)):
        if num_list[i] == num_list[(i+offset) % len(num_list)]:
            n += num_list[i]
    return n

# Read in number list
with open(fn, 'r') as file:
    num_list = [ int(c) for c in file.readline().rstrip("\n") ]

print(f"Part 1 is {compute(num_list, 1)}")
print(f"Part 2 is {compute(num_list, len(num_list) // 2)}")
