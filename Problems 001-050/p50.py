from utils import primesTo, isPrime

LIMIT = 1_000_000


def maxSum(limit: int, primes: list[int]) -> tuple[int, int]:
    res = 0
    mres = 0

    b = 0
    while primes[b] < limit // 2:
        psum = primes[b]
        e = b + 1
        while psum <= limit:
            psum += primes[e]
            e += 1
            if isPrime(psum) and (e - b) > res:
                res = e - b
                mres = psum
        b += 1
    return res, mres


primes = primesTo(LIMIT)
print(maxSum(LIMIT, primes))
