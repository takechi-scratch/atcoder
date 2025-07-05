# 解説AC。
# 同じ文字列が重複して現れることがあるので注意！！

import random

class RollingHash:
    MOD = (1 << 61) - 1
    B = random.randint(2, 1 << 30)

    MASK30 = (1 << 30) - 1
    MASK31 = (1 << 31) - 1
    MASK61 = MOD

    def __init__(self, S: str):
        self.n = n = len(S)
        self.prefix = prefix = [0] * (n + 1)
        self.power = power = [1] * (n + 1)
        b = RollingHash.B
        for i in range(n):
            c = ord(S[i])
            prefix[i + 1] = self._mod(self._multiply(prefix[i], b) + c)
            power[i + 1] = self._mod(self._multiply(power[i], b))

    def get(self, l: int = 0, r: int = 0) -> int:
        if r <= 0: r += self.n
        if not 0 <= l < r <= self.n:
            raise IndexError("index out of range")

        return self._mod(self.prefix[r] - self._multiply(self.power[r - l], self.prefix[l]))

    def _multiply(self, a: int, b: int) -> int:
        au = a >> 31
        ad = a & RollingHash.MASK31
        bu = b >> 31
        bd = b & RollingHash.MASK31
        mid = ad * bu + au * bd
        midu = mid >> 30
        midd = mid & RollingHash.MASK30
        return au * bu * 2 + midu + (midd << 31) + ad * bd

    def _mod(self, x: int) -> int:
        xu = x >> 61
        xd = x & RollingHash.MASK61
        res = xu + xd
        if res >= RollingHash.MOD:
            res -= RollingHash.MOD
        return res

    def __getitem__(self, item):
        if not isinstance(item, (slice, int)):
            raise TypeError("index must be int or slice")

        if isinstance(item, int):
            if item < 0:
                item += self.n
            if not 0 <= item < self.n:
                raise IndexError("index out of range")
            return self.prefix[item]

        if item.step is not None:
            raise ValueError("this can't be set step")

        return self.get(item.start, item.stop)

# --------------------------

from collections import defaultdict

Q = int(input())

X_hashes: defaultdict[int, set[str]] = defaultdict(set)
Y_hashes: defaultdict[int, defaultdict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
Y = defaultdict(int)
ans = 0

for _ in range(Q):
    query = input().split()
    s = query[1]
    s_hash = RollingHash(s)

    if query[0] == "1":
        X_hashes[len(s) - 1].add(s_hash.get())

        for x in Y_hashes[len(s) - 1][s_hash.get()]:
            ans -= Y[x]
            Y[x] = 0

        Y_hashes[len(s) - 1][s_hash.get()] = []

    else:
        for i in range(len(s)):
            now_hash = s_hash[0 : i + 1]
            if now_hash in X_hashes[i]:
                break

        else:
            Y[s] += 1
            ans += 1
            for i in range(len(s)):
                Y_hashes[i][s_hash[0 : i + 1]].append(s)

    print(ans)
