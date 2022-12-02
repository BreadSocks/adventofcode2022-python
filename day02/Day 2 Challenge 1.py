rules = {
    "X": {"A": 3, "B": 0, "C": 6},  # rock
    "Y": {"A": 6, "B": 3, "C": 0},  # paper
    "Z": {"A": 0, "B": 6, "C": 3}  # scissors
}
points = {"X": 1, "Y": 2, "Z": 3}

games = [x.split(" ") for x in open("input.txt").read().splitlines()]
results = []
for game in games:
    results.append(rules[game[1]][game[0]] + points[game[1]])
print(results)
print(sum(results))