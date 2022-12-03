from conftest import example, puzzle_input
from day03.day3 import part1, part2

current_day = "day03"


def test_sample_part1():
    assert part1(example(current_day)) == 157


def test_part1():
    assert part1(puzzle_input(current_day)) == 7727


def test_sample_part2():
    assert part2(example(current_day)) == 70


def test_part2():
    assert part2(puzzle_input(current_day)) == 2609
