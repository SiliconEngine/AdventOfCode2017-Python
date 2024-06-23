#!/usr/bin/python
"""Advent of Code 2017, Day 18, Part 1 and Part 2

https://adventofcode.com/2017/day/18

We're given a program with certain operations. For Part 1, execute the program and
stop at the 'rcv' instruction. For Part 2, simulate two CPUs running at the same
time passing data back and forth, and count the number of send operations.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'instr.dat'

class CPU:
    def __init__(self, prog, id_value):
        self.program = prog
        self.pc = 0
        self.regs = defaultdict(int)
        self.regs['p'] = self.id = id_value
        self.inp_queue = [ ]
        self.other_cpu = None
        self.send_count = 0
        self.save_freq = -1

    def set_other(self, other_cpu):
        self.other_cpu = other_cpu

    def is_wait(self):
        return len(self.inp_queue) == 0

    def send(self, v):
        self.inp_queue.append(v)

    # Execute program until it has to wait or it stops.
    # In Part 1 mode, it returns at the first rcv operation.
    def exec(self):
        get = lambda p: self.regs[p] if p.isalpha() else int(p)

        while self.pc >= 0 and self.pc < len(prog):
            op, p1, p2 = (prog[self.pc] + [''])[:3]
            if op == 'snd':
                if self.other_cpu != None:      # Part 2 mode
                    self.other_cpu.send(get(p1))
                    self.send_count += 1
                else:                           # Part 1 mode
                    self.save_freq = get(p1)
            elif op == 'rcv':
                if self.other_cpu != None:      # Part 2 mode
                    if len(self.inp_queue) == 0:
                        return 'wait'
                    self.regs[p1] = self.inp_queue.pop(0)
                else:                           # Part 1 mode
                    return self.save_freq
            elif op == 'set': self.regs[p1] = get(p2)
            elif op == 'add': self.regs[p1] += get(p2)
            elif op == 'mul': self.regs[p1] *= get(p2)
            elif op == 'mod': self.regs[p1] %= get(p2)
            elif op == 'jgz':
                if get(p1) > 0:
                    self.pc += get(p2)-1

            self.pc += 1

        return 'stop'

with open(fn, 'r') as file:
    prog = [ line.rstrip().split() for line in file ]

# Part 1
cpu = CPU(prog, 0)
print(f"Part 1 is {cpu.exec()}")

# Part 2
cpu0 = CPU(prog, 0)
cpu1 = CPU(prog, 1)
cpu0.set_other(cpu1)
cpu1.set_other(cpu0)

while True:
    state0, state1 = cpu0.exec(), cpu1.exec()
    if (state0, state1) == ('stop', 'stop') or (cpu0.is_wait() and cpu1.is_wait()):
        break

print(f"Part 2 is {cpu1.send_count}")
