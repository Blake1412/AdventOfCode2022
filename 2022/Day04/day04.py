pairs = open("data.txt").read().split("\n")


def part1():
    count = 0
    for pair in pairs:
        one_start = int(pair.split(",")[0].split("-")[0])
        two_start = int(pair.split(",")[1].split("-")[0])
        one_end = int(pair.split(",")[0].split("-")[1])
        two_end = int(pair.split(",")[1].split("-")[1])

        if one_start >= two_start and one_end <= two_end:
            count += 1
        elif two_start >= one_start and two_end <= one_end:
            count += 1
    return count


def part2():
    count = 0
    for pair in pairs:
        one_start = int(pair.split(",")[0].split("-")[0])
        two_start = int(pair.split(",")[1].split("-")[0])
        one_end = int(pair.split(",")[0].split("-")[1])
        two_end = int(pair.split(",")[1].split("-")[1])

        if one_start <= two_end and two_start <= one_end:
            count += 1
    return count


print(part1())
print(part2())
