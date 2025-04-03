N = int(input())

from functools import lru_cache

@lru_cache(maxsize=None)
def f(x):
    assert x >= 0
    if x == 0:
        return 1
    else:
        return f(x // 2) + f(x // 3)

print(f(N))
