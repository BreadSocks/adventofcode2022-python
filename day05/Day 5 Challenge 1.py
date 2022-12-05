from collections import defaultdict
parts = open("input.txt").read().split("\n\n")


def instructions():
    movements = []
    for line in parts[1].splitlines():
        amount_place_split = line.split(" from ")
        amount = int(amount_place_split[0].split("move ")[1])
        origin = int(amount_place_split[1].split(" to ")[0])
        destination = int(amount_place_split[1].split(" to ")[1])
        movements.append([amount, origin, destination])
    return movements


def grid():
    places = [int(x) for x in parts[0].splitlines()[-1].split()]
    # grid_dict = defaultdict.fromkeys(places, [])
    grid_dict = defaultdict(list)
    # grid_dict = dict.fromkeys(places, [])
    lines = parts[0].splitlines()[:-1]
    print(lines)
    for line in lines:
        parsed = [line[char] for char in range(1, len(places) * 4, 4)]
        for index, something in enumerate(parsed):
            if something != " ":
                grid_dict[index + 1].append(something)
    return dict(grid_dict)


places = grid()
# amount, origin, destination
for instruction in instructions():
    amount = instruction[0]
    origin = instruction[1]
    destination = instruction[2]
    for x in range(0, amount):
        places[destination].insert(0, places[origin].pop(0))
    print(places)
#
print(places)
print("".join([places[x][0] for x in range(1, len(places.keys()) + 1)]))
