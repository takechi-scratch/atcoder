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

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

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

# -----------------------

N, M = [int(x) for x in input().split()]
unionfind = DSU(N)

sides = [[] for _ in range(N)]
shareable = [[] for _ in range(N)]  # キーが値行きのやつを持ってる
shareable_num = [[] for _ in range(N)]
for i in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].append(b)
    sides[b].append(a)
    if unionfind.same(a, b):
        shareable[a].append(b)
        shareable_num[a].append(i + 1)
    else:
        unionfind.merge(a, b)

groups = unionfind.groups()
print(len(groups) - 1)

group_shareable = [[] for _ in range(len(groups))]
group_shareable_num = [[] for _ in range(len(groups))]
for i, group in enumerate(groups):
    for j in group:
        group_shareable[i].extend(shareable[j])
        group_shareable_num[i].extend(shareable_num[j])

min_ok = 0
for i in range(len(groups)):
    if min_ok >= len(groups) - 1:
        exit()

    for j in range(len(group_shareable[i])):
        ans_from = group_shareable[i][j]
        ans_num = group_shareable_num[i][j]
        if min_ok + 1 == i:
            print(ans_num, ans_from + 1, groups[0][0] + 1)
            # unionfind.merge(ans_from, groups[0][0]) # あとけす
        else:
            print(ans_num, ans_from + 1, groups[min_ok + 1][0] + 1)
            # unionfind.merge(ans_from, groups[min_ok + 1][0]) # あとけす
        min_ok += 1

        if min_ok >= len(groups) - 1:
            exit()
