from atcoder.dsu import DSU
from collections import defaultdict

H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]


def get_id(i: int, j: int):
    return i * W + j


unionfind = DSU(H * W)
for i in range(H):
    for j in range(W):
        if j + 1 < W and A[i][j] == A[i][j + 1]:
            unionfind.merge(get_id(i, j), get_id(i, j + 1))
        if i + 1 < H and A[i][j] == A[i + 1][j]:
            unionfind.merge(get_id(i, j), get_id(i + 1, j))


color_groups: dict[int, tuple[defaultdict[int, int], set[int]]] = {}
for i in range(H):
    for j in range(W):
        group_id = unionfind.leader(get_id(i, j))
        if group_id not in color_groups:
            color_groups[group_id] = (defaultdict(int), set([group_id]))

        around_scores, used_leaders = color_groups[group_id]
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            if not (0 <= i + di < H and 0 <= j + dj < W):
                continue

            if unionfind.leader(get_id(i + di, j + dj)) in used_leaders:
                continue

            used_leaders.add(unionfind.leader(get_id(i + di, j + dj)))
            around_scores[A[i + di][j + dj]] += unionfind.size(get_id(i + di, j + dj))

ans = 1
for leader_id, group in color_groups.items():
    if len(group[0].values()) > 0:
        extend_score = max(group[0].values())
    else:
        extend_score = 0
    ans = max(ans, unionfind.size(leader_id) + extend_score)

print(ans)
