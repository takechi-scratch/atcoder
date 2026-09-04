from atcoder.lazysegtree import LazySegTree

N = int(input())
S = list(input())
Q = int(input())

A = [0]
for x in S:
    if x == "A":
        A.append(A[-1] + 1)
    else:
        A.append(A[-1] - 1)

A.pop(0)
lst = LazySegTree(
    lambda x, y: min(x, y),
    1 << 60,
    lambda x, y: x + y,
    lambda x, y: x + y,
    0,
    A,
)


for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        i, c = int(query[1]) - 1, query[2]
        if S[i] == c:
            continue
        if c == "A":
            lst.apply(i, N, 2)
        else:
            lst.apply(i, N, -2)
        S[i] = c

    else:
        l, r = int(query[1]) - 1, int(query[2])
        border = 0
        if l >= 1:
            border = lst.get(l - 1)
        print("Yes" if lst.prod(l, r) >= border else "No")
