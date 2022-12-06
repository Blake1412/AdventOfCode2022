datastream = open("data.txt").readline()


def part1():
    for i in range(len(datastream) - 4):
        if len(set(datastream[i:i + 4])) == 4:
            return i + 4


def part2():
    for i in range(len(datastream) - 14):
        if len(set(datastream[i:i + 14])) == 14:
            return i + 14


print(part1())
print(part2())
