rucksacks = open("data.txt").read().split("\n")


def part1():
    total = 0
    for rucksack in rucksacks:
        compartment_one, compartment_two = set(rucksack[:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:])
        value = ord(compartment_one.intersection(compartment_two).pop())
        total += value - 96 if value > 96 else value - 38
    return total


def part2():
    total = 0
    for group in [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]:
        value = ord(set(group[0]).intersection(group[1]).intersection(group[2]).pop())
        total += value - 96 if value > 96 else value - 38
    return total


print(part1())
print(part2())
