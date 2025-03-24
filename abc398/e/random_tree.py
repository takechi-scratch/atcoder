from random import randint

from atcoder.dsu import DSU

N = int(input())
unionfind = DSU(N)
i = 0

while i < N - 1:
    a, b = randint(0, N - 1), randint(0, N - 1)
    if a == b:
        continue
    elif a > b:
        a, b = b, a

    if unionfind.same(a, b):
        continue

    print(a + 1, b + 1)
    unionfind.merge(a, b)
    i += 1
