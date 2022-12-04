from conftest import example, puzzle_input
from day04.day4 import part1, part2

current_day = "day04"


def test_sample_part1():
    assert part1(example(current_day)) == 2


def test_part1():
    assert part1(puzzle_input(current_day)) == 530


def test_sample_part2():
    assert part2(example(current_day)) == 4


def test_part2():
    assert part2(puzzle_input(current_day)) == 903
