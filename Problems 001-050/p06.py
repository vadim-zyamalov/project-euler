def sosq(n: int) -> int:
    assert n > 0
    return n * (n + 1) * (2 * n + 1) // 6


def sqos(n: int) -> int:
    assert n > 0
    return (n * (n + 1) // 2) ** 2


print(sqos(100) - sosq(100))
