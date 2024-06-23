# Advent of Code 2017 solutions written in Python.
## Author: Tim Behrendsen

Link: https://adventofcode.com/2017/

Advent of Code is a series of puzzles over 25 days, each with a part 1 and
part 2. The difficulty roughly rises each day, with the later puzzles often
requiring some tricky algorithms to solve.

For these solutions, the various days are in separate directories, with the
data files.

### Advent of Code 2017, Day 1, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/1

Given a list of digits, calculate the sum of digits that have the same digit at an
offset (wrapping around the end). Part 1, offset is 1. For part 2, offset is half
the length.

### Advent of Code 2017, Day 2, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/2

Given a spreadsheet of numbers, first calculate the sum of the differences
of the highest and lowest numbers for each row. For part 2, figure out which
pair in each row are evenly divisible and total up those quotients.

### Advent of Code 2017, Day 3, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/3

Given a path through squares that are a spiral, part 1 calculates the distance at
a certain number of squares. For part 2, each square contains the sum of the values
of the surrounding squares, and we need to find the first total that exceeds the
target number.

### Advent of Code 2017, Day 4, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/4

Given a list of pass phrases, part 1 counts how many have unique words. Part 2 counts how
many phrases don't have words that are anagrams.

### Advent of Code 2017, Day 5, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/5

Given a list of "jump offsets", follow the chain until it's outside the offset list. For Part 1,
the offset is incremented by one after each jump. For Part 2, the offset is either incremented
or decremented, depending on the value.

### Advent of Code 2017, Day 6, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/6

Given a set of "block counts", figure out which block has the highest count,
then redistribute that count to the other blocks. For Part 1, figure out when
the cycle repeats to any prior state. For Part 2, continue after that and see
when that repeated one repeats again.

### Advent of Code 2017, Day 7, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/7.

Input data is a nested list of nodes in a tree structure. Part 1 figures out which node
is the root node. For Part 2, each node has a weight, and all the children of a parent have
to have the same total weight (including their own children). Finds the inconsistent node and
figures out what weight needs to be set in the node to fix it.

### Advent of Code 2017, Day 8, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/8

We're given a list of instructions to parse that describe increment/decrement operations on
registers (if a condition is met). Part 1 is figure out the highest register value at the
end. Part 2 is the highest value that was computed during processing.

### Advent of Code 2017, Day 9, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/9

Given a stream of characters, parse and identify "garbage" based on given rules.
Part 1 counts the number of "groups". Part 2 counts the number of characters
identified has garbage.

### Advent of Code 2017, Day 10, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/10

Implement an unusual hashing function.

### Advent of Code 2017, Day 11, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/11

Given a hexagonal grid and a list of moves, Part 1 calculates the number of steps it ends up
from the original. In Part 2 calculates the furthest it ever was during the travel.

### Advent of Code 2017, Day 12, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/12

We're given a tree of "pipes". Part 1 calculates the number of unique pipes connected
to pipe #0. Part 2 calculates the number of unique unrelated groups to don't connect
to each other.

### Advent of Code 2017, Day 13, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/13

The data is a "firewall" with scanners that repeat in various given cycles. Part 1
calculates a "severity score" of when we pass over a slot where the scanner is hitting.
Part 2 calculates what delay we need for the cycles to align to allow us to get through
without a scanner hitting us.

### Advent of Code 2017, Day 14, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/14

Using the "knot hash" algorithm from Day 10, create a grid of 0s and 1. Part 1
computes the total number of 1s. Part 2 computes the total number of contiguous
regions.

### Advent of Code 2017, Day 15, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/15

Given two number generators, count the number of times the lower 16 bits
match. Part 1 and Part 2 has some variations in how the numbers are generated.

### Advent of Code 2017, Day 16, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/16

Starting with a sequence of letters, perform "dance moves" to cycle the letters.
Part 1 executes the pattern once. Part 2 predicts the pattern after 1 billion moves.

### Advent of Code 2017, Day 17, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/17

Process insertions into a buffer using a certain pattern. For Part 1, it displays
the value after '2017', with 2017 iterations. For Part 2, it has to simulate
50M iterations and display the number after 0, and so it needed a shortcut.

### Advent of Code 2017, Day 18, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/18

We're given a program with certain operations. For Part 1, execute the program and
stop at the 'rcv' instruction. For Part 2, simulate two CPUs running at the same
time passing data back and forth, and count the number of send operations.

### Advent of Code 2017, Day 19, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/19

Follow an ascii-based tube and accumulate the letters along the way. Part 1 displays the
letters, and Part 2 display the total path length.

### Advent of Code 2017, Day 20, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/20

Given a list particles, Part 1 simulates the movement and figures out which
one is consistently the closest. Part 2 figures out how many particles are left
after collisions are tracked.

### Advent of Code 2017, Day 21, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/21

Given a list of transformation rules for a 2D grid pattern, apply them according to
the puzzle rules. For part 1, do five transformations, and 18 for part 2.

### Advent of Code 2017, Day 22, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/22

We're given a set of rules for how a virus moves around a map spreading an infection.
Part 1 calculates the number of new infections after 10,000 iterations. Part 2 uses
slightly more complex rules and 10M iterations.

This was really about the data structure, which uses a coordinate hash to keep track
of the grid.

### Advent of Code 2017, Day 23, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/23

We're given a program with certain operations, similar to Day 18, but a bit different.
For Part 1, execute the program and count the number of 'mul' instructions. For Part 2,
we have to analyze the algorithm and deduce a way to make it faster to get the final
answer.

### Advent of Code 2017, Day 24, Part 1 and Part 2

Link: https://adventofcode.com/2017/day/24

Given a list of components with socket ends, Part 1 computes the highest "strength"
combination of components. Part 2 computes the highest strength of the longest chain
of components.

### Advent of Code 2017, Day 25

Link: https://adventofcode.com/2017/day/25

Given instruction for a turing machine, execute the instructions and count the
number of one values written onto the tape

