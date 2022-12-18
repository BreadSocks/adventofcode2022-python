def part1(file):
    parts = list(open(file).read())
    return loop(parts, 4)


def part2(file):
    parts = list(open(file).read())
    return loop(parts, 14)


def loop(parts, number):
    for index, letter in enumerate(parts):
        to_check = parts[index + 1:index + number]
        to_check.insert(0, letter)
        if len(to_check) == len(set(to_check)):
            return index + number
