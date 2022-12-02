rules = {
    "X": {"A": 'C', "B": 'A', "C": 'B'},  # lose
    "Y": {"A": 'A', "B": 'B', "C": 'C'},  # draw
    "Z": {"A": 'B', "B": 'C', "C": 'A'}  # win
}
rules2 = {
    "X": {"A": 3, "B": 1, "C": 2},  # lose
    "Y": {"A": 1, "B": 2, "C": 3},  # draw
    "Z": {"A": 2, "B": 3, "C": 1}  # win
}
decision = {"X": 0, "Y": 3, "Z": 6}

games = [x.split(" ") for x in open("input.txt").read().splitlines()]
results = []
for game in games:
    results.append(rules2[game[1]][game[0]] + decision[game[1]])
print(sum(results))
