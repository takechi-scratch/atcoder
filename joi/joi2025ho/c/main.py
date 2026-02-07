# まだWA。式変形から解法を考える練習をしたい...。

from bisect import bisect_left, bisect_right
import typing


# Codon提出用のライブラリコピペ
# https://github.com/not522/ac-library-python
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class SegTree:
    def __init__(
        self,
        op: typing.Callable[[int, int], int],
        e: int,
        v: list[int],
    ) -> None:
        self._op = op
        self._e = e

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: int) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> int:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> int:
        return self._d[1]

    def max_right(self, left: int, f: typing.Callable[[int], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[int], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


N, M, P = [int(x) for x in input().split()]

# assert P <= 100 or N <= 50

from_companies = [[] for _ in range(N)]
all_companies = set()
for _ in range(M):
    a, b, c = [int(x) - 1 for x in input().split()]
    from_companies[b].append(c)
    all_companies.add(c)

[x.sort() for x in from_companies]
all_companies = list(sorted(all_companies))
companies_table = {x: i for i, x in enumerate(all_companies)}
PC = len(all_companies)

# いもす法に似た最大値の更新
least_ok = list(range(PC))  # 圧縮後でとる
for C in from_companies[1:]:
    before = 0
    for x in C:
        least_ok[before] = max(least_ok[before], companies_table[x])
        before = companies_table[x] + 1

    if before < PC:
        least_ok[before] = 10**18

for i in range(1, PC):
    least_ok[i] = max(least_ok[i], least_ok[i - 1])

for i in range(PC):
    if least_ok[i] >= 10**18:
        continue
    # ここで実際の会社番号に直す
    least_ok[i] = all_companies[least_ok[i]]

# llを決めた時の長さのスコアだけをセグ木で持っておく
least_ok_st = SegTree(
    lambda x, y: min(x, y),
    10**18,
    [r - all_companies[l] if r < 10**18 else 10**18 for l, r in enumerate(least_ok)],  # lが展開前、rが展開後
)

Q = int(input())
for _ in range(Q):
    l, r, x = [int(x) for x in input().split()]
    l, r = l - 1, r - 1

    ans = 10**18
    ll = bisect_right(least_ok, r)
    if least_ok[ll] != r:
        ll -= 1
    # rが変わらない中で、llはどこまで下げていいか
    if ll >= 0:
        ans = l - all_companies[ll]
    if ll < 0 or ll >= PC or all_companies[ll] < l:
        # llをあげた時のスコアをセグ木から取得
        ans = min(
            ans,
            least_ok_st.prod(max(0, ll), bisect_left(all_companies, l) + 1) - (r - l),
        )

    print("Yes" if ans <= x else "No")
