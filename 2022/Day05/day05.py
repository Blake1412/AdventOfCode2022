crate_stacks, rearrangements = [line.split("\n") for line in open("bigboy.txt").read().split("\n\n")]
stacks = {}
instructions = [[int(x) for x in rearrangement.split(" ")[1::2]] for rearrangement in rearrangements]


def generate():
    stacks.clear()
    for box in crate_stacks[:-1]:
        for i in range(1, len(box), 4):
            if box[i] != " ":
                stacks.setdefault(i//4 + 1, []).insert(0, box[i])


def part1():
    for instruction in instructions:
        amount, stack_from, stack_to = instruction
        for _ in range(amount):
            stacks[stack_to].append(stacks[stack_from].pop())

    top = [' '] * (len(stacks))
    for k, v in stacks.items():
        top[k - 1] = v[-1]
    return "".join(top)


def part2():
    for instruction in instructions:
        amount, stack_from, stack_to = instruction
        for amount in range(amount, 0, -1):
            stacks[stack_to].append(stacks[stack_from].pop(len(stacks[stack_from]) - amount))

    top = [' '] * (len(stacks))
    for k, v in stacks.items():
        top[k - 1] = v[-1]
    return "".join(top)


generate()
print(part1())
generate()
print(part2())
