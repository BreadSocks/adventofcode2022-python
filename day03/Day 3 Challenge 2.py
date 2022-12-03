import string

lines = open("input.txt").read().splitlines()
scores = dict()
priorities = []
groups = []
group = []

for index, char in enumerate(list(string.ascii_lowercase + string.ascii_uppercase)):
    scores[char] = index + 1


for line in lines:
    group.append(line)
    middle = int(len(line) / 2)
    part1 = list(line[:middle])
    part2 = list(line[-middle:])
    visited = set()
    dupes = set(part1).intersection(part2)
    if len(dupes) > 1:
        print("crap")
    priorities.append(list(dupes)[0])
    if len(group) == 3:
        dupes = set(group[0]).intersection(group[1]).intersection(group[2])
        groups.append(list(dupes)[0])
        group.clear()

print(sum([scores[x] for x in priorities]))
print(sum([scores[x] for x in groups]))
