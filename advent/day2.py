from shared import read_puzzle_input
import math

puzzle_input = read_puzzle_input(2)
puzzle_input = puzzle_input.splitlines()

def advent2_1():
    return sum([2*y[0]*y[1] + 2*y[1]*y[2] + 2*y[2]*y[0] + math.prod(sorted(y)[0:2]) for y in [list(map(int,x.split("x"))) for x in puzzle_input]])


def advent2_2():
    return sum([y[0] * 2 + y[1] * 2 + math.prod(y) for y in [sorted(list(map(int,x.split("x")))) for x in puzzle_input]])


print("\n\n*Advent 2:*")
print("\nPart 1:")
print(advent2_1())
print("\nPart 2:")
print(advent2_2())
