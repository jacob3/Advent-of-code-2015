from shared import read_puzzle_input

puzzle_input = read_puzzle_input(1)


def advent1_1():
    return sum(direction_list())


def advent1_2():
    dirs = direction_list()
    return [x for x, y in enumerate(puzzle_input) if sum(dirs[0:x]) == -1][0]


def direction_list():
    return [1 if x == "(" else -1 for x in puzzle_input]


print("\n\n*Advent 1:*")
print("\nPart 1:")
print(advent1_1())
print("\nPart 2:")
print(advent1_2())
