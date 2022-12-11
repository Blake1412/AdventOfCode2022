import re

monkeys = [[re.findall('\\d+|\\*|\\+', x) for x in y.splitlines()] for y in open("data.txt").read().split("\n\n")]
product = 1
for monkey in monkeys:
    product *= int(monkey[3][0])


def part1():
    inspected_items = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for monkey in monkeys:
            inspected_items[int(monkey[0][0])] += len(monkey[1])
            i = 0
            while i < len(monkey[1]):
                item = int(monkey[1][i])
                multiply = monkey[2][0] == '*'
                y = item if len(monkey[2]) == 1 else int(monkey[2][1])
                z = int(monkey[3][0])
                a = int(monkey[4][0])
                b = int(monkey[5][0])

                if multiply:
                    item = (item * y // 3)
                    receiving_monkey = a if item % z == 0 else b
                else:
                    item = (item + y) // 3
                    receiving_monkey = a if item % z == 0 else b
                monkeys[receiving_monkey][1].append(item)
                monkey[1].pop(0)
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]


def part2():
    inspected_items = [0 for _ in range(len(monkeys))]
    for _ in range(10000):
        for monkey in monkeys:
            inspected_items[int(monkey[0][0])] += len(monkey[1])
            i = 0
            while i < len(monkey[1]):
                item = int(monkey[1][i])
                multiply = monkey[2][0] == '*'
                y = item if len(monkey[2]) == 1 else int(monkey[2][1])
                z = int(monkey[3][0])
                a = int(monkey[4][0])
                b = int(monkey[5][0])

                if multiply:
                    item = item * y % product
                    receiving_monkey = a if item % z == 0 else b
                else:
                    item = item + y
                    receiving_monkey = a if item % z == 0 else b
                monkeys[receiving_monkey][1].append(item)
                monkey[1].pop(0)
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]


# print(part1())
print(part2())
