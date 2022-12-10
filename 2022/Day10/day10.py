instructions = [instruction.split() for instruction in open("data.txt").read().splitlines()]


def part1():
    register_x = 1
    cycle = 1
    signal_strengths = [0 for _ in range(6)]
    for instruction in instructions:
        cycle += 1
        check_cycle(cycle, register_x, signal_strengths)
        if instruction[0] == 'addx':
            cycle += 1
            register_x += int(instruction[1])
            check_cycle(cycle, register_x, signal_strengths)
    return sum(signal_strengths)


def part2():
    register_x = 1
    cycle = 1
    row = 0
    crt = [[' ' for _ in range(40)] for _ in range(6)]
    sprite = [register_x - 1, register_x, register_x + 1]
    for instruction in instructions:
        crt[row][cycle - 1] = '#' if cycle - 1 in sprite else '.'
        cycle += 1
        if cycle > 40:
            cycle = 1
            row += 1
            if row > 5:
                break
        if instruction[0] == 'addx':
            crt[row][cycle - 1] = '#' if cycle - 1 in sprite else '.'
            register_x += int(instruction[1])
            sprite = [register_x - 1, register_x, register_x + 1]
            cycle += 1
            if cycle > 40:
                cycle = 1
                row += 1
                if row > 5:
                    break
    for row in crt:
        print(row)


def check_cycle(cycle: int, register_x: int, signal_strengths: []):
    if cycle > 220:
        return
    if (cycle - 20) % 40 == 0:
        signal_strengths[cycle // 40] = cycle * register_x


print(part1())
part2()
