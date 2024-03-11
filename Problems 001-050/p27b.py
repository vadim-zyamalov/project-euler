from utils import isPrime, primesTo


def solve(limit: int) -> tuple[int, int]:
    bs = primesTo(limit)

    maxn = 0
    ma, mb = 0, 0

    for a in range(-999, 1000):
        for b in bs:
            n = 0
            while isPrime(n**2 + a * n + b):
                n += 1
            if (n - 1) > maxn:
                maxn = n - 1
                ma, mb = a, b

    return (ma, mb)


a, b = solve(1000)
print(f"a={a}, b={b} : {a*b}")
