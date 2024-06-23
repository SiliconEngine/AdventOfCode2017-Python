#!/usr/bin/python
"""Advent of Code 2017, Day 20, Part 1 and Part 2

https://adventofcode.com/2017/day/20

Given a list particles, Part 1 simulates the movement and figures out which
one is consistently the closest. Part 2 figures out how many particles are left
after collisions are tracked.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

import re
from collections import defaultdict

fn = 'test.dat'
fn = 'particles.dat'

def part1(particles):
    work = [ { k: v.copy() for k, v in p.items() } for p in particles ]
    closest_idx = None
    count = 0
    while count < 1000:
        new_idx, new_closest = None, None
        for idx, p in enumerate(work):
            for i in range(3):
                p['v'][i] += p['a'][i]
                p['p'][i] += p['v'][i]

            dist = sum(map(abs, p['p']))
            if new_closest == None or dist < new_closest:
                new_closest, new_idx = dist, idx

        # If closest particle doesn't change after awhile, use that one
        if closest_idx == None or closest_idx != new_idx:
            count = 0
            closest_idx = new_idx
        else:
            count += 1

    return closest_idx

def part2(particles):
    work = [ { k: v.copy() for k, v in p.items() } for p in particles ]
    for p in work:
        p['active'] = True
    no_count = 0
    while no_count < 1000:
        collide = defaultdict(list)
        for p in (p for p in work if p['active']):
            for i in range(3):
                p['v'][i] += p['a'][i]
                p['p'][i] += p['v'][i]
            collide[tuple(p['p'])].append(p)

        # If no collisions after awhile, that's the count
        had_coll = False
        for p_list in (a for a in collide.values() if len(a) > 1):
            had_coll = True
            for p in p_list:
                p['active'] = False

        no_count = no_count+1 if not had_coll else 0

    return sum(p['active'] for p in work)

with open(fn, 'r') as file:
    particles = [{ 'p': a[0:3], 'v': a[3:6], 'a':a[6:9] }
        for a in (list(map(int, re.findall('[\d-]+', line))) for line in file) ]

print(f"Part 1 is {part1(particles)}")
print(f"Part 2 is {part2(particles)}")
