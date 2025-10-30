# 解説AC。波長でリストを作れる、っていう制約を見逃してはいけない。
# 波長でDP的にデータを持ち、東から順番に処理することで計算量を落とせる。
# 処理の順番とデータ構造は一致しなくていいよね、ってお話。

MOD = 10**9 + 7

import typing


# https://github.com/not522/ac-library-python
class FenwickTree:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            self.data[p - 1] %= MOD
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        right = min(right, self._n)
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            s %= MOD
            r -= r & -r

        return s


N, L = [int(x) for x in input().split()]
towers = [[int(x) for x in input().split()] for _ in range(N)]

A_max = max(x[0] for x in towers)
B_max = max(x[1] for x in towers)
out_wave_counts = FenwickTree(max(A_max, B_max))

ans = 0
for a, b in towers:
    catches = out_wave_counts.sum(a - 1, a + L)
    ans += catches + 1
    ans %= MOD
    out_wave_counts.add(b - 1, catches + 1)

print(ans)
