def solve(raw_N: int, M: int, raw_sides: list[list[int]], W: int, holidays: list[list[str]]):
    # Wごとで並列してグラフを作る
    # そこでdfsしてループが見つかればヨシ！

    N = raw_N * W
    sides = [[] for _ in range(N)]
    for i in range(raw_N):
        for day in range(W):
            if holidays[i][day] == "o" and holidays[i][(day + 1) % W] == "o":
                sides[i + raw_N * day].append(i + raw_N * ((day + 1) % W))

    for now_node in range(raw_N):
        for next_node in raw_sides[now_node]:
            for day in range(W):
                if holidays[now_node][day] == "o" and holidays[next_node][(day + 1) % W] == "o":
                    sides[now_node + raw_N * day].append(next_node + raw_N * ((day + 1) % W))

    visited = [False] * N

    def dfs(now: int, route: set[int]):
        for next_node in sides[now]:
            if next_node in route:
                return True
            if visited[next_node]:
                continue

            visited[next_node] = True
            route.add(next_node)
            if dfs(next_node, route):
                return True

            route.remove(next_node)

        return False

    for i in range(raw_N):
        if len(sides[i]) > 0:
            visited[i] = True
            if dfs(i, {i}):
                return True

    return False


T = int(input())
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    sides = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(x) - 1 for x in input().split()]
        sides[a].append(b)
        sides[b].append(a)
    W = int(input())
    holidays = [list(input()) for _ in range(N)]

    print("Yes" if solve(N, M, sides, W, holidays) else "No")
