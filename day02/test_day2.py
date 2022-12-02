from conftest import example, puzzle_input
from day02.day2 import part1, part2

current_day = "day02"


def test_sample_part1():
    assert part1(example(current_day)) == 15


def test_part1():
    assert part1(puzzle_input(current_day)) == 12679


def test_sample_part2():
    assert part2(example(current_day)) == 12


def test_part2():
    assert part2(puzzle_input(current_day)) == 14470
