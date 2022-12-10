moves = [move.split(" ") for move in open("data.txt").read().split("\n")]
directions = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}


def part1():
    positions = set()
    positions.add('00')
    head, tail = [0, 0], [0, 0]
    for move in moves:
        dx, dy = directions[move[0]]
        amount = move[1]
        for _ in range(int(amount)):
            head[0] += dx
            head[1] += dy
            move_knot(tail, head)
            positions.add("".join(str(x) for x in tail))
    return len(positions)


def part2():
    positions = set()
    positions.add('00')
    knots = [[0, 0] for _ in range(10)]
    for move in moves:
        dx, dy = directions[move[0]]
        amount = move[1]
        for _ in range(int(amount)):
            knots[0][0] += dx
            knots[0][1] += dy
            for i in range(1, len(knots)):
                move_knot(knots[i], knots[i - 1])
            positions.add("".join(str(x) for x in knots[-1]))
    return len(positions)


def move_knot(tail: [int], head: [int]):
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    adx, ady = abs(dx), abs(dy)
    if adx != 1 and adx + ady == 2:
        dx, dy = dx / 2, dy / 2
    elif adx + ady >= 3:
        dx, dy = 1 if dx > 0 else -1, 1 if dy > 0 else -1
    else:
        dx, dy = 0, 0
    tail[0] += dx
    tail[1] += dy


print(part1())
print(part2())
