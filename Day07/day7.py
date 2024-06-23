#!/usr/bin/python
"""Advent of Code 2017, Day 7, Part 1 and Part 2

https://adventofcode.com/2017/day/7.

Input data is a nested list of nodes in a tree structure. Part 1 figures out which node
is the root node. For Part 2, each node has a weight, and all the children of a parent have
to have the same total weight (including their own children). Finds the inconsistent node and
figures out what weight needs to be set in the node to fix it.

See test.dat for test data and counts.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict
import re

fn = 'tower.dat'

regs = defaultdict(int)
most = 0

# Part 1: Find the base of the tower, which is the node name which is not contained
# in any of the sub node lists.
def find_base(towers):
    all_subs = set(sub for node in towers.values() for sub in node[2])
    return next(name for name in towers.keys() if name not in all_subs)

# Fill in total weight for each node, which is the sum of itself + sub nodes
def calc_total_weights(towers, base):
    node = towers[base]
    node[3] = node[1] + sum(calc_total_weights(towers, sub) for sub in node[2])
    return node[3]

# Find node that has children with inconsistent weight and return amount needed to fix
def find_bad_node(towers, base):
    calc_total_weights(towers, base)

    node = towers[base]
    while True:
        # For node, figure out how many children have each weight
        counts = defaultdict(int)
        for sub in node[2]:
            counts[towers[sub][3]] += 1

        # If only one weight, we've reached a good node, so parent is final bad
        # 'target_num' had the good weight from the parent node.
        if len(counts) == 1:
            return target_num - sum(towers[sub][3] for sub in node[2])

        # Continue down the child with the inconsistent weight
        k = list(counts.keys())
        bad_weight, target_num = (k[0], k[1]) if counts[k[0]] == 1 else (k[1], k[0])
        new_name = next(sub for sub in node[2] if towers[sub][3] == bad_weight)
        node = towers[new_name]

with open(fn, 'r') as file:
    towers = { }
    for line in file:
        name, weight, _, subs = re.findall(r'(\w+) \((\d+)\)( -> )?(.*)', line)[0]
        towers[name] = [ name, int(weight), [ sub for sub in subs.split(', ') if sub != '' ], 0 ]

base = find_base(towers)
print(f"Part 1 is {base}")

fix_amt = find_bad_node(towers, base)
print(f"Part 2 is {fix_amt}")
