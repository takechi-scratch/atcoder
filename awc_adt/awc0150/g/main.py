N, Q = [int(x) for x in input().split()]
T = [int(x) - 1 for x in input().split()]
ans = [-1] * N

for start in range(N):
    if ans[start] != -1:
        continue

    dfs = [start]
    dfs_set = {start}
    now = start
    hit = -1
    while True:
        next_node = T[now]
        if next_node in dfs_set:
            hit = next_node
            hit_index = dfs.index(hit)
            loop_size = len(dfs) - hit_index

            for i in range(len(dfs)):
                ans[dfs[len(dfs) - i - 1]] = max(loop_size, i + 1)

            break
        if ans[next_node] != -1:
            base = ans[next_node]
            for i in range(len(dfs)):
                ans[dfs[len(dfs) - i - 1]] = i + base + 1

            break

        dfs_set.add(next_node)
        dfs.append(next_node)
        now = next_node


for _ in range(Q):
    print(ans[int(input()) - 1])
