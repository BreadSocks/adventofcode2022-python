count = 0
lines = [x.split(",") for x in open("input.txt").read().splitlines()]
for line in lines:
    left = [int(x) for x in line[0].split("-")]
    right = [int(x) for x in line[1].split("-")]
    if left[0] <= right[0] and left[1] >= right[1]:
        count += 1
    elif left[0] >= right[0] and left[1] <= right[1]:
        count += 1

print(count)

