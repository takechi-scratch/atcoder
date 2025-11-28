from atcoder.fenwicktree import FenwickTree

N, M, Q = [int(x) for x in input().split()]
items = [[int(x) for x in input().split()] for _ in range(N)]
type_items = [[] for _ in range(M)]

for i, item in enumerate(items):
    type_items[item[1] - 1].append(i)

item_sum_tree = FenwickTree(N)
for i, item in enumerate(items):
    item_sum_tree.add(i, item[0])

query = [[int(x) for x in input().split()] for _ in range(Q)]
T_query_index = [[] for _ in range(M)]
for i, x in enumerate(query):
    T_query_index[x[0] - 1].append(i)

ans = [None] * Q

for T in range(M):
    for i in type_items[T]:
        item_sum_tree.add(i, -items[i][0] // 2)

    for i in T_query_index[T]:
        _, L, R = query[i]
        ans[i] = int(item_sum_tree.sum(L - 1, R))

    for i in type_items[T]:
        item_sum_tree.add(i, items[i][0] // 2)

print(*ans, sep="\n")
