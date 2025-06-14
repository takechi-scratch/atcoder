import sys
sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
costs = [[] for _ in range(N)]

cycle_addable = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    sides[a].append(b)
    costs[a].append(w)
    if a == b:
        cycle_addable[a].append(w)

visited = [False] * N
finished = [False] * N
path: list[tuple[int, int]] = []
def dfs(now, score):
    visited[now] = True

    for i, next_node in enumerate(sides[now]):
        if finished[next_node]:
            continue

        if visited[next_node]:
            cycle = []
            pick_index = -1
            while True:
                picked = path[pick_index]
                pick_index -= 1
                cycle.append(picked)
                if picked[0] == next_node:
                    break

            can_rotate_score = (score ^ costs[now][i]) ^ cycle[-1][1]
            for node, _ in cycle:
                cycle_addable[node].append(can_rotate_score)

            continue

        path.append((next_node, score ^ costs[now][i]))
        dfs(next_node, score ^ costs[now][i])
        path.pop()

    finished[now] = True

path.append((0, 0))
dfs(0, 0)

if not visited[-1]:
    print(-1)
    exit()

best_record =

print(min(min_xors[-1]))
