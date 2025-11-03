# ふつうにDFSをして、次の頂点を最小のものから選んでいけばいい！

def solve(N: int, X: int, Y: int, sides: list[list[int]]):
    # 非再帰DFSでルートを記録するには、ルートの削除コマンドをDFSにのせる
    dfs = [(1, X)]
    route = []
    visited = [False] * N
    while len(dfs) > 0:
        op, now = dfs.pop()
        if op == -1:
            deleted = route.pop()
            # 一応確認（nowを探してからdeleteするのは遅いので）
            assert deleted == now
            continue

        visited[now] = True
        route.append(now)
        if now == Y:
            return [x + 1 for x in route]

        # ここで今の頂点を削除するコマンドを追加。
        # dfsは最後に追加したものから取り出されるため、
        # 削除コマンドは他の辺をすべて見た後に実行される。
        dfs.append((-1, now))
        for next_node in sorted(sides[now], reverse=True):
            if visited[next_node]:
                continue

            dfs.append((1, next_node))

    raise RuntimeError


# マルチテストケース用のテンプレート作ってみた

T = int(input())
for _ in range(T):
    N, M, X, Y = [int(x) for x in input().split()]
    X -= 1
    Y -= 1
    sides = [[] for _ in range(N)]
    for _ in range(M):
        u, v = [int(x) - 1 for x in input().split()]
        sides[u].append(v)
        sides[v].append(u)

    ans = solve(N, X, Y, sides)
    if ans in [True, False]:
        print("Yes" if ans else "No")
    elif isinstance(ans, int) or isinstance(ans, str):
        print(ans)
    else:
        print(*ans)
