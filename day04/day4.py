def generate(file):
    count = 0
    overlapping = 0
    lines = [x.split(",") for x in open(file).read().splitlines()]

    for line in lines:
        left = [int(x) for x in line[0].split("-")]
        right = [int(x) for x in line[1].split("-")]
        if left[0] <= right[0] and left[1] >= right[1]:
            count += 1
        elif left[0] >= right[0] and left[1] <= right[1]:
            count += 1
        numbers_left = list(range(left[0], left[1] + 1))
        numbers_right = list(range(right[0], right[1] + 1))
        if len(set(numbers_left + numbers_right)) != len(numbers_left + numbers_right):
            overlapping += 1

    return count, overlapping


def part1(file):
    count, overlaps = generate(file)
    return count


def part2(file):
    count, overlaps = generate(file)
    return overlaps
