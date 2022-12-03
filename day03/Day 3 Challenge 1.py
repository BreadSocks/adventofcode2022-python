import string

lines = open("input.txt").read().splitlines()
scores = dict()
priorities = []

for index, char in enumerate(list(string.ascii_lowercase + string.ascii_uppercase)):
    scores[char] = index + 1


for line in lines:
    middle = int(len(line) / 2)
    part1 = list(line[:middle])
    part2 = list(line[-middle:])
    visited = set()
    dupes = set(part1).intersection(part2)
    if len(dupes) > 1:
        print("crap")
    priorities.append(list(dupes)[0])

print(sum([scores[x] for x in priorities]))
