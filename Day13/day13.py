#!/usr/bin/python
"""Advent of Code 2017, Day 13, Part 1 and Part 2

https://adventofcode.com/2017/day/13

The data is a "firewall" with scanners that repeat in various given cycles. Part 1
calculates a "severity score" of when we pass over a slot where the scanner is hitting.
Part 2 calculates what delay we need for the cycles to align to allow us to get through
without a scanner hitting us.

See test.dat for test data and scan.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict
from itertools import count

fn = 'test.dat'
fn = 'scan.dat'

seq = [ ]

# Calculate severity, or stop early if we get a hit.
# Cycles are up and then down. A cycle of 5 is: 0 1 2 3 4 3 2 1
def calc_severity(firewall, delay=0, stop=False):
    severity = 0
    for pos, cycle in seq:
        cpos = (pos + delay) % ((cycle-1)*2)
        m = cpos if cpos < cycle else ((cycle-1)*2)-cpos
        if m == 0:
            if stop:
                return -1
            severity += (pos * cycle)

    return severity

firewall = defaultdict(int)
with open(fn, 'r') as file:
    for line in file:
        d, r = line.rstrip('\n').split(': ')
        firewall[int(d)] = int(r)

# Boil down position and cycle just to speed things up
seq = [ (pos, cycle) for pos, cycle in firewall.items() ]

# Calculate severity score from hits starting with no delay.
print(f"Part 1 is {calc_severity(firewall)}")

# Try delays until no hits.
for delay in count(1):
    if calc_severity(firewall, delay, True) == 0:
        break
print(f"Part 2 is {delay}")
