file = "input.txt"
parts = list(open(file).read())

for index, letter in enumerate(parts):
    to_check = parts[index + 1:index + 13 + 1]
    to_check.insert(0, letter)
    if len(to_check) == len(set(to_check)):
        print(index + 14)
        break

