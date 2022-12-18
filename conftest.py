import os

import pytest as pytest


def example(day):
    return os.getcwd() + "/" + day + "/example.txt"


def example2(day):
    return os.getcwd() + "/" + day + "/further_example_1.txt"


def example3(day):
    return os.getcwd() + "/" + day + "/further_example_2.txt"


def example4(day):
    return os.getcwd() + "/" + day + "/further_example_3.txt"


def example5(day):
    return os.getcwd() + "/" + day + "/further_example_4.txt"


def puzzle_input(day):
    return os.getcwd() + "/" + day + "/input.txt"

