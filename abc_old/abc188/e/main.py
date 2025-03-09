# x < y という制約があるので、dfsのstartは昇順に決めてOK
# （「有向辺の途中から探索開始」ってことにはならない）

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

sides = [[] for _ in range(N)]
for _ in range(M):
    x, y = [int(x) - 1 for x in input().split()]
    sides[x].append(y)

ans = -10 ** 18
visited = [False] * N
root_min_values = [10 ** 18] * N  # 各頂点ごとに持っておくように

for start in range(N):
    if visited[start]:
        continue

    visited[start] = True
    dfs = [start]

    while len(dfs) > 0:
        now = dfs.pop()
        now_min = min(root_min_values[now], A[now])  # この頂点までで買うときの最小価格に変える

        for next_node in sides[now]:
            if visited[next_node]:
                ans = max(ans, A[next_node] - now_min)
                if root_min_values[next_node] <= now_min:  # 合流するまでにもっと小さいものを見つけているかも
                    continue

            ans = max(ans, A[next_node] - now_min)
            visited[next_node] = True
            dfs.append(next_node)
            root_min_values[next_node] = now_min

print(ans)

# 別の考え方
# グラフがそのままDAGになっている→DPと考えてOK
