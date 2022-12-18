from conftest import example, puzzle_input
from day07.day7 import part1, part2

current_day = "day07"


def test_sample_part1():
    assert part1(example(current_day)) == 95437


def test_part1():
    assert part1(puzzle_input(current_day)) == 1350966


def test_sample_part2():
    assert part2(example(current_day)) == 24933642


def test_part2():
    assert part2(puzzle_input(current_day)) == 6296435
