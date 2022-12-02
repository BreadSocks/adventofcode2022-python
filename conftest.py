import os


def example(day):
    return os.getcwd() + "/" + day + "/example.txt"


def puzzle_input(day):
    return os.getcwd() + "/" + day + "/input.txt"


def test_file(day, name):
    return os.getcwd() + "/" + day + "/" + name
