#!/usr/bin/python
"""Advent of Code 2017, Day 25

https://adventofcode.com/2017/day/25

Given instruction for a turing machine, execute the instructions and count the
number of one values written onto the tape

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

import re
from collections import defaultdict

fn = 'test.dat'
fn = 'turing.dat'

states = { }
with open(fn, 'r') as file:
    begin_state = (file.readline())[15:16]
    steps = int(re.findall('\d+', file.readline())[0])
    if_value = None

    for line in file:
        line = line.strip()
        if line[0:8] == 'In state':
            state = line[9:10]
            states[(state, 0)] = [ ]
            states[(state, 1)] = [ ]
        elif line[0:2] == 'If':
            if_value = int(line[24:25])
        elif line[0:7] == '- Write':
            states[(state, if_value)].append(('W', int(line[18: 19])))
        elif line[0:10] == '- Move one':
            states[(state, if_value)].append(('M', line[23: 24]))
        elif line[0:15] == '- Continue with':
            states[(state, if_value)].append(('C', line[22: 23]))

tape = defaultdict(int)
pos, state = 0, begin_state
for step in range(steps):
    for i in states[(state, tape[pos])]:
        if i[0] == 'W':
            tape[pos] = i[1]
        elif i[0] == 'M':
            pos = pos+1 if i[1] == 'r' else pos-1
        else:   # Must be C
            state = i[1]

print(f"Part is: {sum(t == 1 for t in tape.values())}")
