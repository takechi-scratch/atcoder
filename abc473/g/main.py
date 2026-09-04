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


N, K = [int(x) for x in input().split()]
mc = ModComb()
mc._calc_inv_factor(N)

print(mc.mod_comb(N, K - N) * mc.inv_factor[N] * pow(K - N, -1, mod) % 998244353)
