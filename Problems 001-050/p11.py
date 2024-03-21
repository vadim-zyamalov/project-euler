from math import prod


def check(r: int, c: int, grid: list[list[int]]) -> int:
    res = prod(grid[r][c + i] for i in range(4))
    res = max(res, prod(grid[r + i][c] for i in range(4)))
    res = max(res, prod(grid[r + i][c + i] for i in range(4)))
    if r >= 3:
        res = max(res, prod(grid[r - i][c + i] for i in range(4)))

    return res


def solve(grid: list[list[int]]) -> int:
    nr, nc = len(grid), len(grid[0])

    return max(check(r, c, grid) for r in range(nr - 3) for c in range(nc - 3))


with open("0011_grid.txt", "r") as f:
    GRID = [
        list(map(int, line.strip().split()))
        for line in f.read().strip().split("\n")
    ]

print(solve(GRID))
