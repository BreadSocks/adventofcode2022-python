elves = sorted([[int(y) for y in x.splitlines()] for x in open("input.txt").read().split("\n\n")], key=sum, reverse=True)
# Part 1
print(sum(elves[0]))
# Part 2
print(sum([sum(x) for x in elves[:3]]))
