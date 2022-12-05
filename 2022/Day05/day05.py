crate_stacks, rearrangements = [line.split("\n") for line in open("data.txt").read().split("\n\n")]
stacks = {}
for box in crate_stacks[:-1]:
    for i in range(1, len(box), 4):
        if box[i] != " ":
            stacks.setdefault(int(crate_stacks[-1][i]), []).insert(0, box[i])
instructions = [[int(x) for x in rearrangement.split(" ")[1::2]] for rearrangement in rearrangements]


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
        while amount > 0:
            stacks[stack_to].append(stacks[stack_from].pop(len(stacks[stack_from]) - amount))
            amount -= 1

    top = [' '] * (len(stacks))
    for k, v in stacks.items():
        top[k - 1] = v[-1]
    return "".join(top)


# print(part1())
# print(part2())
