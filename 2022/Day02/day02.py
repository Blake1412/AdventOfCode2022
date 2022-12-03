rounds = open("data.txt").read().split("\n")


def part1():
    outcomes = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    return sum(outcomes[round] for round in rounds)


def part2():
    outcomes = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    return sum(outcomes[round] for round in rounds)


print(part1())
print(part2())
