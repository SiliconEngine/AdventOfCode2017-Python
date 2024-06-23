#!/usr/bin/python
"""Advent of Code 2017, Day 4, Part 1 and Part 2

https://adventofcode.com/2017/day/4

Given a list of pass phrases, part 1 counts how many have unique words. Part 2 counts how
many phrases don't have words that are anagrams.

See phrases.dat for full data.

Author: Tim Behrendsen
"""

fn = 'phrases.dat'

def no_anagrams(p):
    s = set([ ''.join(sorted(w)) for w in p ])
    return len(s) == len(p)

def is_unique(p):
    return len(set(p)) == len(p)

def part1(phrases):
    return sum([ is_unique(p) for p in phrases ])

def part2(phrases):
    return sum([ no_anagrams(p) for p in phrases ])

with open(fn, 'r') as file:
    phrases = [ line.rstrip('\n').split(' ') for line in file ]

print(f"Part 1 count is {part1(phrases)}")
print(f"Part 2 count is {part2(phrases)}")
