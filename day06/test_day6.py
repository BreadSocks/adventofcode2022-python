import pytest

from conftest import example, puzzle_input, example2, example3, example4, example5
from day06.day6 import part1, part2

current_day = "day06"


def test_sample_part1():
    assert part1(example(current_day)) == 7


def test_further_1_part1():
    assert part1(example2(current_day)) == 5


def test_further_2_part1():
    assert part1(example3(current_day)) == 6


def test_further_3_part1():
    assert part1(example4(current_day)) == 10


def test_further_4_part1():
    assert part1(example5(current_day)) == 11


def test_part1():
    assert part1(puzzle_input(current_day)) == 1658


def test_sample_part2():
    assert part2(example(current_day)) == 19


def test_further_1_part2():
    assert part2(example2(current_day)) == 23


def test_further_2_part2():
    assert part2(example3(current_day)) == 23


def test_further_3_part2():
    assert part2(example4(current_day)) == 29


def test_further_4_part2():
    assert part2(example5(current_day)) == 26


def test_part2():
    assert part2(puzzle_input(current_day)) == 2260
