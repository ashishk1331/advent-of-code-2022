lines = ""

with open("input.txt", "r") as file:
    lines = [line for line in file.read().split("\n")]


class Folder(object):
    """ Folder class to represent folders in the tree structure. """

    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent


class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size


def construct(lines):

    root = None
    index = 0

    while index < len(lines):

        command = lines[index].split()

        if command[0] == "$":

            if command[1] == "ls":
                while (index+1 < len(lines)) and (not lines[index+1].startswith("$")):
                    contents = lines[index+1].split()
                    if contents[0].startswith("dir"):
                        root.children.append(Folder(contents[1], root))
                    else:
                        root.children.append(
                            File(contents[1], int(contents[0])))

                    index += 1

            elif command[1] == "cd":

                if command[2] == "..":
                    root = root.parent
                elif command[2] == "/":
                    root = Folder(command[2])
                else:
                    for item in root.children:
                        if item.name == command[2]:
                            root = item
                            break

        index += 1

    while root.parent:
        root = root.parent

    return root


def print_structure(root, level):
    print(
        "|" if level > 0 else "",
        "__"*level,
        root.name,
        f" ({root.size})" if isinstance(root, File) else "",
        sep=""
    )
    if hasattr(root, "children"):
        for child in root.children:
            print_structure(child, level+1)


def at_most_100000(root, ans):
    size = 0

    if hasattr(root, "children"):
        for item in root.children:
            if isinstance(item, File):
                size += item.size
            else:
                size += at_most_100000(item, ans)

    if size <= 100000:
        ans[0] += size

    return size


def optimal_folder(root, array, needed_space):
    size = 0

    if hasattr(root, "children"):
        for item in root.children:
            if isinstance(item, File):
                size += item.size
            else:
                size += optimal_folder(item, array, needed_space)

    if size >= needed_space:
        array.append(size)


def main():
    root = construct(lines)
    # print_structure(root, 0)

    ## PART 1 -> all folders size who are < 100000
    # ans = [0]
    # print(at_most_100000(root, ans))
    # print(ans[0])

    # PART 2 -> optimal solution for deletion
    free_space = 70000000 - 40913445
    needed_space = abs(free_space - 30000000)
    array = []
    optimal_folder(root, array, needed_space)
    print(min(array))


if __name__ == '__main__':
    main()
