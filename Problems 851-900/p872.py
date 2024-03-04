def f(n, k):
    powers = f"{n - k:b}"

    res = n
    nxt = n

    for i, p in enumerate(powers[::-1]):
        p = int(p)
        if p:
            nxt -= 2**i
            res += nxt

    return res


print(f(10**17, 9**17))
