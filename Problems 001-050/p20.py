from utils import fact

res = 0
num = fact(100)

while num:
    num, q = divmod(num, 10)
    res += q

print(res)
