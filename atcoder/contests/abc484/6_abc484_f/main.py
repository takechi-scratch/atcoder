from atcoder.segtree import SegTree

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def op(x, y):
    if x[1] is False or y[1] is False:
        return (-1, False)

    if x[0] == -1:
        return (y[0], True)
    if y[0] == -1:
        return (x[0], True)
    if x[0] == y[0]:
        return x

    return (-1, False)


st = SegTree(op, (-1, True), [(x, True) for x in A])

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        st.set(query[1] - 1, (query[2], True))
    else:
        print("Yes" if st.prod(query[1] - 1, query[2])[1] else "No")
