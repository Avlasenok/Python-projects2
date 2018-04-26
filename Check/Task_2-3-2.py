import math
import itertools


def primes():
    i = 2
    while True:
        if (math.factorial(i - 1) + 1) % i == 0:
            yield i
        i += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))

a = [i + 1 for i in range(4)]
print(a)
a = [i for i in range(4)]
print(a)
a = [i for i in range(5)][1:]
print(a)
a = list(i + 1 for i in range(4))
print(a)