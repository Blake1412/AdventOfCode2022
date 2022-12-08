trees = [[int(x) for x in y] for y in [list(line) for line in open("data.txt").read().split("\n")]]
columns = list(zip(*trees))


def part1():
    count = len(trees) * 2 + len(trees[0]) * 2 - 4
    for row in range(1, len(trees) - 1):
        for col in range(1, len(trees[0]) - 1):
            tree = trees[row][col]
            if tree > max(trees[row][col + 1:]) \
                    or tree > max(trees[row][:col]) \
                    or tree > max(columns[col][:row]) \
                    or tree > max(columns[col][row + 1:]):
                count += 1
    return count


def part2():
    max_score = 0
    for row in range(len(trees)):
        for col in range(len(trees[0])):
            start_tree = trees[row][col]
            score = viewing_distance(trees[row][col + 1:], start_tree) \
                    * viewing_distance(reversed(trees[row][:col]), start_tree) \
                    * viewing_distance(reversed(columns[col][:row]), start_tree) \
                    * viewing_distance(columns[col][row + 1:], start_tree)
            max_score = max(max_score, score)
    return max_score


def viewing_distance(tree_path: [int], start_tree: int):
    score = 0
    for tree in tree_path:
        score += 1
        if tree >= start_tree:
            break
    return score


print(part1())
print(part2())
