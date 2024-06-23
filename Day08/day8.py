#!/usr/bin/python
"""Advent of Code 2017, Day 8, Part 1 and Part 2

https://adventofcode.com/2017/day/8

We're given a list of instructions to parse that describe increment/decrement operations on
registers (if a condition is met). Part 1 is figure out the highest register value at the
end. Part 2 is the highest value that was computed during processing.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'instr.dat'

regs = defaultdict(int)
most = 0

with open(fn, 'r') as file:
    for line in file:
        # Form: gcf dec 135 if esb < 10
        d_reg, incdec, val1, _, t_reg, op, t_val = line.rstrip('\n').split(' ')
        if op == '<': flag = regs[t_reg] < int(t_val)
        elif op == '<=': flag = regs[t_reg] <= int(t_val)
        elif op == '>': flag = regs[t_reg] > int(t_val)
        elif op == '>=': flag = regs[t_reg] >= int(t_val)
        elif op == '==': flag = regs[t_reg] == int(t_val)
        elif op == '!=': flag = regs[t_reg] != int(t_val)
        if flag:
            regs[d_reg] += int(val1) if incdec == 'inc' else 0-int(val1)
            most = max(regs[d_reg], most)

print(f"Part 1 is {max(regs.values())}")
print(f"Part 2 is {most}")
