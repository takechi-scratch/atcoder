# unionfindを使ってうまくやる
# WAのときはランダムテストを心がける！！（時間ギリギリだったのでしょうがないけど）

# aclのライブラリはジャッジでも使えるのでimportでOK
# （使い方には注意！）
from atcoder.dsu import DSU

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)
ans = []

unionfind = DSU(N)
can_go_max = 0
can_go = set([0])

for k in range(N):
    is_same = unionfind.same(0, k)

    for x in sides[k]:
        can_go.add(x)
        if x < k or is_same:
            # 「残しておいて大丈夫な辺」はつなげる
            unionfind.merge(k, x)

    # can_go_maxの更新は1ずつやって問題ない（しゃくとり的な感じ、計算量はO(N+M)で行けるはず）
    while can_go_max < N - 1 and unionfind.same(can_go_max, can_go_max + 1):
        can_go_max += 1

    # 再度unionfindの判定をする
    if can_go_max >= k and unionfind.same(0, k):
        ans.append(str(len(can_go) - k - 1))
    else:
        ans.append("-1")


print("\n".join(ans))
