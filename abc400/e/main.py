# 解説AC。要復習
# 答えの全列挙→にぶたんの流れはOK。

from math import isqrt
from bisect import bisect_right

# 大きな数の平方根はisqrtで
Q = int(input())
query = [isqrt(int(input())) for _ in range(Q)]
max_query = max(query)

# テンプレコード、エラトステネスのふるい
prime_max = max_query
prime_kouho = set(range(2, prime_max))
for i in range(2, isqrt(prime_max) + 1):
    if i not in prime_kouho:
        continue

    j = 2
    while i * j <= prime_max:
        prime_kouho.discard(i * j)
        j += 1

primes = list(sorted(prime_kouho))

# primesの上限値に注意。MAX^2 * 1^2 みたいなのがあるので MAX ** 1/4 ではダメ
# WAポイント！素数の二重ループはTLEのおそれ
# 整数問題ときたら「倍数」でのループに目を向ける

factor_counts = [0] * max_query

for x in primes:
    cur = x - 1
    while True:
        if cur >= max_query:
            break

        factor_counts[cur] += 1
        cur += x


fh_nums = []
for i, x in enumerate(factor_counts):
    if x == 2:
        fh_nums.append(i + 1)

# print(len(fh_nums))

for A in query:
    pos = bisect_right(fh_nums, int(A))
    print(fh_nums[pos - 1] ** 2)
