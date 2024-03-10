def cycleDetect(a: int, b: int) -> tuple[int, int]:
    a %= b
    remainders = [a]

    while (a := (10 * a) % b) not in remainders:
        remainders.append(a)

    mu = remainders.index(a)
    return mu, len(remainders) - mu


print(cycleDetect(1, 983))
