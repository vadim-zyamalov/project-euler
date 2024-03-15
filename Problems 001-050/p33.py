from utils import gcd
import time


def solve() -> int:
    nums = []
    dens = []
    for nr in range(10, 99):
        for dr in range(nr + 1, 100):
            if nr % 10 == 0 and dr % 10 == 0:
                continue
            if nr % 11 == 0 and dr % 11 == 0:
                continue

            nr0, nr1 = nr // 10, nr % 10
            dr0, dr1 = dr // 10, dr % 10

            if nr0 == dr0:
                n, d = nr1, dr1
            elif nr0 == dr1:
                n, d = nr1, dr0
            elif nr1 == dr0:
                n, d = nr0, dr1
            elif nr1 == dr1:
                n, d = nr0, dr0
            else:
                n, d = None, None

            if n is not None and d is not None:
                g0 = gcd(nr, dr)
                g1 = gcd(n, d)

                if nr // g0 == n // g1 and dr // g0 == d // g1:
                    nums.append(n // g1)
                    dens.append(d // g1)

    nr = 1
    dr = 1
    for i in range(4):
        nr *= nums[i]
        dr *= dens[i]

    return dr // gcd(nr, dr)


def solve_forum() -> int:
    nums = 1
    dens = 1

    for x in range(1, 10):
        for y in range(x + 1, 10):
            z, q = divmod(10 * x * y, 9 * x + y)
            if q == 0 and z > x:
                nums *= x
                dens *= z
    for y in range(1, 10):
        for x in range(y + 1, 10):
            z, q = divmod(x * y, 10 * y - 9 * x)
            if q == 0 and z > x:
                nums *= x
                dens *= z

    return dens // gcd(dens, nums)


t0 = time.time()
print(f"{solve()} {time.time() - t0:.4f}")
t0 = time.time()
print(f"{solve_forum()} {time.time() - t0:.4f}")
