from atcoder.dsu import DSU
from collections import Counter


class ModComb:
    def __init__(self, MOD: int = 998244353):
        self.MOD = MOD
        self.factor = [1]
        self.inv_factor = []

    def _calc_factor(self, limit: int):
        for i in range(len(self.factor), limit + 1):
            self.factor.append(self.factor[-1] * i % self.MOD)

    def _calc_inv_factor(self, limit: int):
        self._calc_factor(limit)
        for x in range(len(self.inv_factor), limit + 1):
            self.inv_factor.append(pow(self.factor[x], self.MOD - 2, self.MOD))

    def mod_comb(self, n: int, k: int):
        if not 0 <= k <= n:
            return 0

        self._calc_factor(n)
        self._calc_inv_factor(k)
        self._calc_inv_factor(n - k)

        ans = self.factor[n] * self.inv_factor[k] % self.MOD
        ans = ans * self.inv_factor[n - k] % self.MOD
        return ans


N, M = [int(x) for x in input().split()]
MOD = 998244353
uf = DSU(N)
mc = ModComb()
S = input()
for _ in range(M):
    m, n = [int(x) - 1 for x in input().split()]
    uf.merge(m, n)

exchangable = False
ans = 1
for group in uf.groups():
    parts = [S[i] for i in group]
    if len(parts) > len(set(parts)):
        exchangable = True

    c = Counter(parts)
    now = len(group)
    for _, value in c.items():
        ans *= mc.mod_comb(now, value)
        ans %= MOD
        now -= value

if not exchangable:
    ans *= pow(2, -1, MOD)

print(ans % MOD)
