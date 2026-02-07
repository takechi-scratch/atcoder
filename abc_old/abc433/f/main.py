S = [int(x) for x in list(input())]
N = len(S)
MOD = 998244353

positions = [[i for i in range(N) if S[i] == x] for x in range(10)]


class ModComb:
    def __init__(self, MOD: int = 998244353) -> None:
        self.MOD = MOD
        self.factor: list[int] = [1]
        self.inv_factor: list[int] = []

    def _calc_factor(self, limit: int) -> None:
        for i in range(len(self.factor), limit + 1):
            self.factor.append(self.factor[-1] * i % self.MOD)

    def _calc_inv_factor(self, limit: int) -> None:
        self._calc_factor(limit)
        for x in range(len(self.inv_factor), limit + 1):
            self.inv_factor.append(pow(self.factor[x], self.MOD - 2, self.MOD))

    def mod_comb(self, n: int, k: int) -> int:
        if n < k:
            return 0

        self._calc_factor(n)
        self._calc_inv_factor(k)
        self._calc_inv_factor(n - k)

        ans = self.factor[n] * self.inv_factor[k] % self.MOD
        ans = ans * self.inv_factor[n - k] % self.MOD
        return ans

    def comb_multiplied_sum(self, a: int, b: int) -> int:
        """aC0 * bC1 + aC1 * bC2 + ... + aCb-1 + bCbをmodで計算
        参照: https://manabitimes.jp/math/622
        """
        return self.mod_comb(a + b - 1, b - 1)


mod_comb = ModComb()


ans = 0
for num in range(9):
    search_pos = positions[num] + positions[num + 1]
    search_pos.sort()
    sum_1 = len(positions[num])
    sum_2 = len(positions[num + 1])
    now_1 = 0
    now_2 = sum_2

    for i in search_pos:
        if S[i] == num:
            now_1 += 1
            if now_1 >= 1 and now_2 >= 1:
                ans += mod_comb.comb_multiplied_sum(now_1, now_2)
                ans %= MOD
        else:
            now_2 -= 1


print(ans)
