from conftest import example, puzzle_input
from day05.day5 import part1, part2, generate

current_day = "day05"


def test_sample_part1():
    grid, instructions = generate(example(current_day))
    assert part1(grid, instructions) == "CMZ"


def test_part1():
    grid, instructions = generate(puzzle_input(current_day))
    assert part1(grid, instructions) == "WSFTMRHPP"


def test_sample_part2():
    grid, instructions = generate(example(current_day))
    assert part2(grid, instructions) == "MCD"


def test_part2():
    grid, instructions = generate(puzzle_input(current_day))
    assert part2(grid, instructions) == "GSLCMFBRP"
