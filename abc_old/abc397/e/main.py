# DFSの帰りがけに「それより後に今何個つながってるか」を見て、合わせる
# （木DPというらしい…）

import sys
sys.setrecursionlimit(10 ** 7)
# PyPyでの提出時は忘れずに！！！（CPythonでもACできた）
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")


N, K = [int(x) for x in input().split()]
NK = N * K

sides = [[] for _ in range(NK)]
visited = [False] * NK

for _ in range(NK - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

def dfs(now: int, before: int):
    # pcはpath_countの略
    after_pcs = []

    # 一番下
    if len(sides[now]) == 1 and sides[now][0] == before:
        return 1

    for next_node in sides[now]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        after_pc = dfs(next_node, now)
        # 「これより下でちょうどできた」ときは、今の頂点を考えなくてヨシ
        if after_pc % K == 0:
            continue

        after_pcs.append(after_pc)

    if len(after_pcs) >= 3:
        # どう頑張っても無理
        print("No")
        exit()

    if len(after_pcs) == 0:
        # この頂点を一番下とする
        return 1

    if len(after_pcs) == 1:
        # 必要な1個に今の頂点もつなげる
        return (after_pcs[0] + 1) % K

    # 余りが2個あり、今の頂点と合わせて合体させるとちょうどよくなるとき
    if (after_pcs[0] + after_pcs[1] + 1) % K == 0:
        return 0

    print("No")
    exit()

visited[0] = True
dfs(0, -1)
assert all(visited)

print("Yes")
