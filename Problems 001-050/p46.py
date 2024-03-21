from utils import isPrime


# Для n до 33 мы знаем ответ
def solve(n: int = 33) -> int:
    assert n > 1
    assert n & 1 == 1

    while True:
        n += 2
        if isPrime(n):
            continue

        lim = int(((n - 1) // 2) ** 0.5)

        for i in range(lim, 0, -1):
            if isPrime(n - 2 * i * i):
                break
        else:
            return n


print(solve(33))
