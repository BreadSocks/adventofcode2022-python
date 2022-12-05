from collections import defaultdict


class Instruction:
    def __init__(self, amount, origin, destination):
        self.amount = amount
        self.origin = origin
        self.destination = destination


def instructions(instruction_part):
    movements = []
    for line in instruction_part.splitlines():
        amount_place_split = line.split(" from ")
        instruction = Instruction(int(amount_place_split[0].split("move ")[1]),
                                  int(amount_place_split[1].split(" to ")[0]),
                                  int(amount_place_split[1].split(" to ")[1])
                                  )
        movements.append(instruction)
    return movements


def grid(grid_part):
    places = [int(x) for x in grid_part.splitlines()[-1].split()]
    grid_dict = defaultdict(list)
    lines = grid_part.splitlines()[:-1]
    print(lines)
    for line in lines:
        parsed = [line[char] for char in range(1, len(places) * 4, 4)]
        for index, something in enumerate(parsed):
            if something != " ":
                grid_dict[index + 1].append(something)
    return dict(grid_dict)


def generate(file):
    parts = open(file).read().split("\n\n")
    return grid(parts[0]), instructions(parts[1])


def part1(places, movements):
    for instruction in movements:
        for x in range(0, instruction.amount):
            places[instruction.destination].insert(0, places[instruction.origin].pop(0))
    return "".join([places[x][0] for x in range(1, len(places.keys()) + 1)])


def part2(places, movements):
    for instruction in movements:
        for index, x in enumerate(range(0, instruction.amount)):
            places[instruction.destination].insert(index, places[instruction.origin][index])
        places[instruction.origin] = places[instruction.origin][instruction.amount:]
        print(places)
    return "".join([places[x][0] for x in range(1, len(places.keys()) + 1)])
