sections = open("input.txt").read().split("\n\n")
elves = dict()
for index, section in enumerate(sections):
    elves[index + 1] = [int(x) for x in section.splitlines()]

max = 0
for key, value in elves.items():
    elf = sum(value)
    if elf > max:
        max = elf

print(max)
