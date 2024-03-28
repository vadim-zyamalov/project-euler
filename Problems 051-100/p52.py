def search() -> int:
    n = 2
    while True:
        for p in range(10 ** (n - 1), 10**n // 6 + 1):
            if all(sorted(str(p)) == sorted(str(i * p)) for i in range(2, 7)):
                return p
        n += 1


print(search())
