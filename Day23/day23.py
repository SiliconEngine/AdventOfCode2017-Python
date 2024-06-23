#!/usr/bin/python
"""Advent of Code 2017, Day 23, Part 1 and Part 2

https://adventofcode.com/2017/day/23

We're given a program with certain operations, similar to Day 18, but a bit different.
For Part 1, execute the program and count the number of 'mul' instructions. For Part 2,
we have to analyze the algorithm and deduce a way to make it faster to get the final
answer.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'instr.dat'

# Reduced fast version of algorithm.
def alg():
    a,b,c,d,e,f,g,h = 1,0,0,0,0,0,0,0
    b = 93
    c = b
    if a != 0:
        b *= 100
    b += 100000
    c = b + 17000
    while True:
        f = 1
        #print(f"OUTER 1: a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}")

##        for d in range(2, b+1):
##            for e in range(2, b+1):
##                if d * e == b:
##                    f = 0
##                    break
##                if d * e > b:
##                    break
##            if f == 0:
##                break

        # The following is equivalent to the above, because the above is checking if there
        # exists two numbers, d and e, the product of which is 'b'. This is basically
        # checking if there exists an even divisor, which we can reduce to mod = 0.
        for i in range(2, b):
            if b % i == 0:
                f = 0
                break

        if f == 0:
            h += 1
        if b == c:
            return h
        b += 17

class CPU:
    def __init__(self, prog):
        self.program = prog
        self.pc = 0
        self.regs = defaultdict(int)
        self.mul_count = 0

    def exec(self):
        get = lambda p: self.regs[p] if p.isalpha() else int(p)

        while self.pc >= 0 and self.pc < len(prog):
            op, p1, p2 = (prog[self.pc] + [''])[:3]
            if op == 'set': self.regs[p1] = get(p2)
            elif op == 'sub': self.regs[p1] -= get(p2)
            elif op == 'mul':
                self.regs[p1] *= get(p2)
                self.mul_count += 1
            elif op == 'jnz':
                if get(p1) != 0:
                    self.pc += get(p2)-1

            self.pc += 1

        return 'stop'

with open(fn, 'r') as file:
    prog = [ line.rstrip().split() for line in file ]

# Part 1
cpu = CPU(prog)
cpu.exec()
print(f"Part 1 is {cpu.mul_count}")

n = alg()
print(f"Part 2 is {n}")
