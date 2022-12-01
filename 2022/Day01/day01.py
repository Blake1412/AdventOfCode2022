elves = [list(map(int, x)) for x in [elf.split("\n") for elf in open("data.txt").read().split("\n\n")]]


def part1():
    return max(sum(elf) for elf in elves)


def part2():
    return sum(sorted([sum(elf) for elf in elves])[-3:])


print(part1())
print(part2())
