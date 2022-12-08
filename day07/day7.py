from anytree import Node, RenderTree


def generate_filesystem(file):
    lines = open(file).read().splitlines()
    filesystem = Node("")
    current_node = filesystem
    file_sizes = dict()
    folders = dict()

    for index, line in enumerate(lines[1:]):
        line_parts = line.split(" ")
        if line == "$ ls":
            continue
        elif line_parts[0] == "dir":
            Node(line_parts[1], parent=current_node)
        elif line_parts[0].isdigit():
            file = Node(line_parts[1], parent=current_node)
            file_sizes[file] = int(line_parts[0])
        elif line_parts[1] == "cd" and line_parts[2] == "..":
            current_node = current_node.parent
        elif line_parts[1] == "cd":
            for child in current_node.children:
                if child.name == line_parts[2]:
                    current_node = child

    folders[filesystem] = size_of_children(filesystem, file_sizes, folders)
    return filesystem, file_sizes, folders


def print_file_system(filesystem):
    for pre, fill, node in RenderTree(filesystem):
        print("%s%s" % (pre, node.name))


def size_of_children(node, file_sizes, folders):
    node_total = 0
    for child in node.children:
        if len(child.children) > 0:
            amount = size_of_children(child, file_sizes, folders)
            folders[child] = amount
            node_total += amount
        else:
            node_total += file_sizes[child]
    return node_total


def part1(file):
    filesystem, filesizes, folders = generate_filesystem(file)
    return sum([x for x in folders.values() if x <= 100000])


def part2(file):
    filesystem, filesizes, folders = generate_filesystem(file)
    minimum = float("inf")
    free_space = 70000000 - folders[filesystem]
    need = 30000000 - free_space
    for x in folders.values():
        if need <= x < minimum:
            minimum = x

    return minimum
