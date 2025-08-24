# https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
import typing


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n
        self.blacks = [0] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.blacks[x] += self.blacks[y]
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


N, Q = [int(x) for x in input().split()]
dsu = DSU(N)
is_black = [0] * N

for _ in range(Q):
    query = [int(x) - 1 for x in input().split()]
    if query[0] == 0:
        dsu.merge(query[1], query[2])
    elif query[0] == 1:
        v = query[1]
        leader = dsu.leader(v)
        if is_black[v] == 0:
            dsu.blacks[leader] += 1
        else:
            dsu.blacks[leader] -= 1

        is_black[v] = 1 - is_black[v]
    elif query[0] == 2:
        print("Yes" if dsu.blacks[dsu.leader(query[1])] > 0 else "No")
    else:
        raise RuntimeError
