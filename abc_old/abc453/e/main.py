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


N = int(input())
ok_ranges = [[int(x) for x in input().split()] for _ in range(N)]
MOD = 998244353
mcb = ModComb()

partial_oks = [0] * (N + 1)
for l, r in ok_ranges:
    partial_oks[l] += 1
    partial_oks[r + 1] -= 1

for i in range(1, N + 1):
    partial_oks[i] += partial_oks[i - 1]

# 少ない方視点 i番目: 人数がiとN-iのとき、どっちもを範囲に含むやつ
both_oks = [0] * N
for l, r in ok_ranges:
    if not (l <= N // 2 and (N + 1) // 2 <= r):
        continue

    both_oks[max(l, N - r)] += 1

for i in range(1, N):
    both_oks[i] += both_oks[i - 1]

ans = 0
for a_people in range(1, N):
    b_people = N - a_people
    ab = both_oks[min(a_people, b_people)]
    a_sum = partial_oks[a_people]
    b_sum = partial_oks[b_people]

    if ab + (a_sum - ab) + (b_sum - ab) < N:
        continue

    more_a = a_people - (a_sum - ab)
    more_b = b_people - (b_sum - ab)

    ans += mcb.mod_comb(ab, more_a)
    ans %= MOD

print(ans)
