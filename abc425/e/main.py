import subprocess
from collections import Counter
from functools import lru_cache
from math import isqrt
import sys

sys.setrecursionlimit(10**7)


def prime_factorization(x: int) -> list[int]:
    """素因数分解を行う関数

    Args:
        x (int): 素因数分解したい整数

    Returns:
        list[int]: 素因数分解した結果のリスト
    """

    out = subprocess.run(["factor", str(x)], stdout=subprocess.PIPE, check=True).stdout
    return [int(x) for x in out.decode().strip().split(" ")[1:]]


prime_max = 5000
prime_kouho = set(range(2, prime_max))
for i in range(2, isqrt(prime_max) + 1):
    if i not in prime_kouho:
        continue

    j = 2
    while i * j <= prime_max:
        prime_kouho.discard(i * j)
        j += 1

primes = list(sorted(prime_kouho))


@lru_cache(maxsize=None)
def factor_counter(n: int) -> Counter:
    if n <= 1:
        return {}

    ans = factor_counter(n - 1)
    for x in prime_factorization(n):
        ans[x] += 1

    return ans


factor_counter(5000)

T, M = [int(x) for x in input().split()]


for _ in range(T):
    N = int(input())
    C = [int(x) for x in input().split()]
    ans = factor_counter(sum(C)).copy()
    for x in C:
        for key, value in factor_counter(x).items():
            if key > 1:
                ans[key] -= value

    last_ans = 1
    for key, value in ans.items():
        last_ans *= key**value

    print(last_ans % M)
