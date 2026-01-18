# upsolve。3段階の発想が必要
# 1: 等差数列の長さは2つか3つ。Aが偶数の時は2つのみ、奇数の時は長さ3が1つだけとなる
# 2: Aが偶数の時は、半分に分けて小さい順にペアを組んでいくのが最適
# 3: 奇数で長さ3の等差数列を決めたとき、残りでペアを組んだときのAの距離差は、左右でほぼ変わらない
# →セグ木などを使えば、O(logN)で距離差の最大値を出すことができる
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
        v: int,
    ) -> None:
        self._op = op
        self._e = e
        v = [e] * v

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


from bisect import bisect_left
from sys import exit

N = int(input())
A = [int(x) for x in input().split()]

if N % 2 == 0:
    print(min(A[i + N // 2] - A[i] for i in range(N // 2)))
    exit()

dist_score: list[SegTree] = []
for dist in range((N - 3) // 2, (N - 3) // 2 + 4):
    st = SegTree(lambda x, y: min(x, y), 10**18, N - dist)
    for i in range(N - dist):
        st.set(i, A[i + dist] - A[i])

    dist_score.append(st)

ans = -1
for i in range(N - 1):
    for j in range(i + 1, N):
        k = bisect_left(A, A[j] + (A[j] - A[i]))
        if k >= N or A[k] - A[j] != A[j] - A[i]:
            continue

        def pair_pos(x):
            # real_pos -> pair_pos
            return x - int(x >= i) - int(x >= j) - int(x >= k)

        def real_pos(x):
            # pair_pos -> real_pos
            return x + int(x > pair_pos(i)) + int(x > pair_pos(j)) + int(x > pair_pos(k))

        def p(x):
            # real_pos -> 相手のreal_pos
            px = pair_pos(x)
            if px >= (N - 3) // 2:
                return real_pos(px - (N - 3) // 2)
            else:
                return real_pos(px + (N - 3) // 2)

        def calc_dist(x):
            # pair_pos -> real_posのdist
            rx = real_pos(x)
            return abs(rx - p(rx))

        border = [0]  # pair_pos管理
        for target in (i, j, k):
            if pair_pos(target) == pair_pos(target + 1):
                continue

            if calc_dist(pair_pos(target)) != calc_dist(pair_pos(target + 1)):
                border.append(pair_pos(min(target + 1, p(target + 1))))

        border.append((N - 3) // 2)
        border = list(sorted(set(border)))
        now_ans = A[j] - A[i]
        for bi in range(len(border) - 1):
            l, r = real_pos(border[bi]), real_pos(border[bi + 1])
            if l in (i, j, k):
                continue

            while True:
                if r - 1 in (i, j, k):
                    r -= 1
                else:
                    break

            now_ans = min(
                now_ans,
                dist_score[calc_dist(border[bi]) - (N - 3) // 2].prod(l, r),
            )

        ans = max(ans, now_ans)

print(ans)
