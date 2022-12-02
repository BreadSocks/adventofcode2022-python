from conftest import example, puzzle_input
from day01.day1 import part1, part2

current_day = "day01"


def test_sample_part1():
    assert part1(example(current_day)) == 24000


def test_part1():
    assert part1(puzzle_input(current_day)) == 71471


def test_sample_part2():
    assert part2(example(current_day)) == 45000


def test_part2():
    assert part2(puzzle_input(current_day)) == 211189
