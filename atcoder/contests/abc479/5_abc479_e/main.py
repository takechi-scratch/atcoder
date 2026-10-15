# import sys

# sys.setrecursionlimit(10**7)

N = int(input())
sides = [[] for _ in range(N)]
node_counts = [[] for _ in range(N)]
all_sides = [[int(x) - 1 for x in input().split()] for _ in range(N - 1)]
side_ids = {}

i = 1
for a, b in all_sides:
    sides[a].append(b)
    node_counts[a].append(0)
    sides[b].append(a)
    node_counts[b].append(0)

    side_ids[(min(a, b), max(a, b))] = i
    i += 1

ans = [0] * N


def node_count_dfs(now: int, before: int):
    if len(sides[now]) == 1 and sides[now][0] == before:
        return 1

    ans = 0
    for i, next_node in enumerate(sides[now]):
        if next_node == before:
            continue

        node_counts[now][i] = node_count_dfs(next_node, now)
        ans += node_counts[now][i]

    return ans + 1


score_sum = 0


def dfs(now: int, before: int, now_score: int):
    global score_sum
    ans[now] = now_score

    for next_node, next_counts in zip(sides[now], node_counts[now]):
        if before == next_node:
            continue

        if next_counts > N // 2:
            dfs(next_node, now, now_score + side_ids[(min(now, next_node), max(now, next_node))])
        else:
            dfs(next_node, now, now_score - side_ids[(min(now, next_node), max(now, next_node))])

        score_sum += side_ids[(min(now, next_node), max(now, next_node))] * max(next_counts, N - next_counts)


node_count_dfs(0, -1)
dfs(0, -1, 0)
assert (score_sum - sum(ans)) % N == 0
ans_plus = (score_sum - sum(ans)) // N
ans = [x + ans_plus for x in ans]
print(" ".join([str(x) for x in ans]))
