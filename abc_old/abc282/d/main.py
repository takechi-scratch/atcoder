from collections import deque

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

color = [-1] * N

ans = 0
part_nodes = []
for start in range(N):
    if color[start] != -1:
        continue

    color[start] = 0

    side_count = 0
    node_colors = [1, 0]
    bfs = deque([start])

    while len(bfs) > 0:
        now = bfs.popleft()
        ok = True
        for next_side in sides[now]:
            if color[next_side] == color[now]:
                ok = False
                break

            side_count += 1

            if color[next_side] != -1:
                continue

            color[next_side] = 1 - color[now]
            node_colors[color[next_side]] += 1
            bfs.append(next_side)

        if not ok:
            print(0)
            exit()

    # breakされなかった
    assert side_count % 2 == 0
    ans += node_colors[0] * node_colors[1] - side_count // 2
    part_nodes.append(node_colors[0] + node_colors[1])

# 非連結の部分とつなげるとき
# WAポイント！無向グラフで辺を数えるときは2で割る！
unconsolidated = 0
for x in part_nodes:
    unconsolidated += x * (N - x)

print(ans + unconsolidated // 2)
