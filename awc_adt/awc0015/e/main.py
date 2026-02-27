from atcoder.fenwicktree import FenwickTree

N, Q = [int(x) for x in input().split()]
P = [int(x) - 1 for x in input().split()]
query = []
for i in range(Q):
    l, r = [int(x) for x in input().split()]
    query.append([l - 1, r - 1, i])

query.sort(key=lambda x: x[1])

uniques = FenwickTree(N + 1)
before_pos = [-1] * N

ans_count = 0
ans = [0] * Q

for r in range(N):
    uniques.add(before_pos[P[r]] + 1, 1)
    uniques.add(r + 1, -1)
    before_pos[P[r]] = r

    while ans_count < Q and query[ans_count][1] == r:
        ans[query[ans_count][2]] = uniques.sum(0, query[ans_count][0] + 1)
        ans_count += 1

print(*ans, sep="\n")
