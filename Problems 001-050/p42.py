OFFSET = ord("A") - 1


def isTriangle(word: str) -> bool:
    t = sum(map(lambda ch: ord(ch) - OFFSET, word))

    d = 0.25 + 2 * t

    if d <= 0:
        return False

    n = -0.5 + d**0.5
    # нам не нужен корень n == -0.5 - d**0.5

    if n.is_integer():
        return True

    return False


def solve(fname: str) -> int:
    with open(fname, "r") as f:
        res = sum(isTriangle(w.strip('"')) for w in f.read().strip().split(","))

    return res


print(solve("0042_words.txt"))
