rules = {
    "X": {"A": 'C', "B": 'A', "C": 'B'},  # lose
    "Y": {"A": 'A', "B": 'B', "C": 'C'},  # draw
    "Z": {"A": 'B', "B": 'C', "C": 'A'}  # win
}
points = {"A": 1, "B": 2, "C": 3}
decision = {"X": 0, "Y": 3, "Z": 6}

games = [x.split(" ") for x in open("input.txt").read().splitlines()]
results = []
for game in games:
    results.append(points[rules[game[1]][game[0]]] + decision[game[1]])
print(sum(results))
