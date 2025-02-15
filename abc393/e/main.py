# setだとメモ化再帰はできない！なんか使ってみようと思ったけどダメ。

from functools import lru_cache
from math import gcd

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

@lru_cache(maxsize=10 ** 9)
def many_gcd(numbers: set):
    a = numbers.pop()
    if len(numbers) <= 0:
        return a

    return gcd(many_gcd(numbers), a)

assert many_gcd(set([3,6,9])) == 3
