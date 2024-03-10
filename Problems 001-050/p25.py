from math import log10
from utils import fib1

i = 1
while log10(fib1(i)) + 1 < 1000:
    i += 1
print(i)
