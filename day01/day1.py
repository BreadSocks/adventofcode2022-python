def part1(file):
    sorted_elves = elves(file)
    return sum(sorted_elves[0])


def part2(file):
    sorted_elves = elves(file)
    return sum([sum(x) for x in sorted_elves[:3]])


def elves(file):
    return sorted([[int(y) for y in x.splitlines()] for x in open(file).read().split("\n\n")], key=sum, reverse=True)
