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
A = [int(x) for x in input().split()]
mc = ModComb()
MOD = 998244353

if N == 1:
    print(A[0] ** 2 % MOD)
elif N == 2:
    if K == 1:
        print((A[0] ** 2 + A[1] ** 2) % MOD)
    else:
        print(sum(A) ** 2 % MOD)
elif K == 1:
    print(sum(x * x for x in A) % MOD)

else:
    squared_sum = sum(x * x for x in A) % MOD
    pair_all_sum = ((sum(A) % MOD) ** 2 - squared_sum) * pow(2, -1, MOD) % MOD

    print((mc.mod_comb(N - 1, K - 1) * squared_sum + 2 * mc.mod_comb(N - 2, K - 2) * pair_all_sum) % MOD)
