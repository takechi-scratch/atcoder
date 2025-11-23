# MODをとる二項係数の計算
# 前計算にO(max(n, k, n - k)), 本計算にO(1)


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
        if n < k:
            return 0

        self._calc_factor(n)
        self._calc_inv_factor(k)
        self._calc_inv_factor(n - k)

        ans = self.factor[n] * self.inv_factor[k] % self.MOD
        ans = ans * self.inv_factor[n - k] % self.MOD
        return ans

    def comb_multiplied_sum(self, a: int, b: int):
        """aC0 * bC1 + aC1 * bC2 + ... + aCb-1 + bCbを計算
        参照: https://manabitimes.jp/math/622
        """
        return self.mod_comb(a + b - 1, b - 1)
