import string

scores = dict([(char, index + 1) for index, char in enumerate(list(string.ascii_lowercase + string.ascii_uppercase))])


def generate(file):
    priorities = []
    groups = []
    group = []
    for line in open(file).read().splitlines():
        group.append(line)
        middle = int(len(line) / 2)
        priorities.append(list(set(list(line[:middle])).intersection(list(line[-middle:])))[0])
        if len(group) == 3:
            groups.append(list(set(group[0]).intersection(group[1]).intersection(group[2]))[0])
            group.clear()
    return priorities, groups


def part1(file):
    priorities, groups = generate(file)
    return sum([scores[x] for x in priorities])


def part2(file):
    priorities, groups = generate(file)
    return sum([scores[x] for x in groups])
