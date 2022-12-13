grid = [list(line) for line in open("data.txt").read().splitlines()]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def part1():
    return shortest_path((0, 0))


def part2():
    shortest = 100000
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'a':
                new_shortest = shortest_path((r, c))
                if new_shortest is not None:
                    shortest = min(shortest, new_shortest)
    return shortest


def shortest_path(start: tuple[int, int]):
    count = 0
    queue = [start]
    visited = [start]
    nodes_in_next, nodes_in_current = 0, 1

    while len(queue) > 0:
        r, c = queue.pop()
        if grid[r][c] == 'E':
            return count
        start = ord('z') if grid[r][c] == 'S' else ord(grid[r][c])
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr >= len(grid) or rr < 0 or cc >= len(grid[0]) or cc < 0 or (rr, cc) in visited:
                continue
            neighbour = ord('z') + 1 if grid[rr][cc] == 'E' else ord(grid[rr][cc])
            if neighbour > start + 1:
                continue
            queue.insert(0, (rr, cc))
            visited.append((rr, cc))
            nodes_in_next += 1
        nodes_in_current -= 1
        if nodes_in_current == 0:
            nodes_in_current = nodes_in_next
            nodes_in_next = 0
            count += 1


print(part1())
print(part2())
