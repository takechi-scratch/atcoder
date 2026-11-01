from collections import deque, Counter, defaultdict

N = int(input())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

C = [int(x) for x in input().split()]


def tree_bfs(start: int) -> list[int]:
    bfs = deque([start])
    dists = [10**18] * N
    dists[start] = 0
    while len(bfs) > 0:
        now = bfs.popleft()
        for next_node in sides[now]:
            if dists[next_node] < 10**18:
                continue

            dists[next_node] = dists[now] + 1
            bfs.append(next_node)

    return dists


zero_dists = tree_bfs(0)
diameter_left = zero_dists.index(max(zero_dists))

left_dists = tree_bfs(diameter_left)
diameter = max(left_dists)
diameter_right = left_dists.index(diameter)

right_dists = tree_bfs(diameter_right)


if diameter % 2 == 1:
    center_1 = min(i for i in range(N) if left_dists[i] == diameter // 2 and right_dists[i] == (diameter + 1) // 2)
    center_2 = min(i for i in range(N) if right_dists[i] == diameter // 2 and left_dists[i] == (diameter + 1) // 2)

    c1_dists = tree_bfs(center_1)
    c1_counter = Counter(C[i] for i in range(N) if c1_dists[i] == (diameter + 1) // 2)
    c2_dists = tree_bfs(center_2)
    c2_counter = Counter(C[i] for i in range(N) if c2_dists[i] == (diameter + 1) // 2)

    ans = 0
    for key in set(c1_counter.keys()) | set(c2_counter.keys()):
        ans += c1_counter[key] * c2_counter[key]

    print(ans)
else:
    center = min(i for i in range(N) if left_dists[i] == diameter // 2 and right_dists[i] == diameter // 2)
    partial_tree_colors: list[defaultdict] = []

    dists = [10**18] * N
    for start in sides[center]:
        partial_tree_colors.append(defaultdict(int))

        bfs = deque([start])
        dists[start] = 1
        while len(bfs) > 0:
            now = bfs.popleft()

            if dists[now] == diameter // 2:
                partial_tree_colors[-1][C[now]] += 1

            for next_node in sides[now]:
                if dists[next_node] < 10**18 or next_node == center:
                    continue

                dists[next_node] = dists[now] + 1
                bfs.append(next_node)

        # partial_tree_colors.append(Counter(C[i] for i in dists.keys() if dists[i] == diameter // 2))

    color_counts = [[] for _ in range(N)]
    for x in partial_tree_colors:
        for color in x.keys():
            if x[color] > 0:
                color_counts[color].append(x[color])

    ans = 0
    for A in color_counts:
        ans += (sum(A) ** 2 - sum(x**2 for x in A)) // 2

    print(ans)
