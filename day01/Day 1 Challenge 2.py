sections = open("input.txt").read().split("\n\n")
elves = dict()
for index, section in enumerate(sections):
    elves[index + 1] = [int(x) for x in section.splitlines()]

max = 0
for key, value in elves.items():
    elf = sum(value)
    if elf > max:
        max = elf

order = dict(sorted(elves.items(), key=lambda item: sum(item[1]), reverse=True))
top3 = dict(list(order.items())[:3])
print(top3)
total = 0
for x in top3:
    total += sum(list(top3[x]))
print(total)
