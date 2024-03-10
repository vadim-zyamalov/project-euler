def maxTotal(pyramid: list[list[int]]) -> int:
    """
    Destructive max trace computation
    """
    nlev = len(pyramid)

    for i in range(nlev - 2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])

    return pyramid[0][0]


with open("p67.txt", "r") as f:
    pyr = list(
        list(map(int, line.split())) for line in f.read().strip().split("\n")
    )

    print(maxTotal(pyr))
