commands = open("data.txt").read().split("\n")
directories = []
directory_stack = []

for command in commands:
    args = command.split(" ")
    if args[0] == '$':
        if args[1] == 'cd':
            if args[2] == '..':
                directories.append(directory_stack.pop())
            else:
                directory_stack.append(0)
    elif args[0] != 'dir':
        directory_stack = [directory + int(args[0]) for directory in directory_stack]
directories.extend(directory_stack)


def part1():
    return sum(directory for directory in directories if directory <= 100000)


def part2():
    max_size = max(directories)
    return min(directory for directory in directories if directory >= 700000000 - (3000000000 - max_size))


print(part1())
print(part2())
