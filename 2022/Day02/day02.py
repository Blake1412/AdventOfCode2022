rounds = list([round.split(" ") for round in open("data.txt").read().split("\n")])


def part1():
    total = 0
    for round in rounds:
        opponent = ord(round[0]) - 64
        player = ord(round[1]) - 64 - 23
        total += get_round_score(opponent, player)
    return total


def part2():
    total = 0
    for round in rounds:
        opponent = ord(round[0]) - 64
        outcome = ord(round[1]) - 64 - 23
        match outcome:
            case 1:
                match opponent:
                    case 1:
                        player = 3
                    case _:
                        player = opponent - 1
            case 2:
                player = opponent
            case 3:
                match opponent:
                    case 3:
                        player = 1
                    case _:
                        player = opponent + 1
        total += get_round_score(opponent, player)
    return total


def get_round_score(opponent: int, player: int):
    score = player
    match (player - opponent):
        case 0:
            score += 3
        case -2 | 1:
            score += 6
    return score


print(part1())
print(part2())
