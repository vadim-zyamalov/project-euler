def nameScore(i: int, line: str) -> int:
    return i * sum(map(lambda c: ord(c) - 64, line))


with open("0022_names.txt", "r", encoding="utf8") as f:
    names = f.read().strip().split(",")
names = sorted(map(lambda x: x.strip('"'), names))

res = 0
for i, line in enumerate(names):
    res += nameScore(i + 1, line)
print(res)
