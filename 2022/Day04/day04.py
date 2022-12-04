pairs = [[int(num) for num in item.replace(",", "-").split("-")] for item in open("data.txt").read().split("\n")]


def part1():
    return len([pair for pair in pairs if pair[0] >= pair[2] and pair[1] <= pair[3] or pair[2] >= pair[0] and pair[3] <= pair[1]])


def part2():
    return len([pair for pair in pairs if pair[0] <= pair[3] and pair[2] <= pair[1]])


print(part1())
print(part2())
