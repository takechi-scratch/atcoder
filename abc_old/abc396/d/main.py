import sys
sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]
sides_labels = [{} for _ in range(N)]
labels = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = [int(x) for x in input().split()]
    sides_labels[u - 1][v - 1] = w
    sides_labels[v - 1][u - 1] = w

ans = 10 ** 21
visited = set()

def visit(now: int, visited: set[int], score):
    global ans

    if now == N - 1:
        ans = min(ans, score)
        return

    for next_node in range(N):
        if next_node in visited:
            continue

        if next_node not in sides_labels[now]:
            continue

        visit(next_node, visited | {next_node}, score ^ sides_labels[now][next_node])

visit(0, set([0]), 0)
print(ans)
