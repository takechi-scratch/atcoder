def solve(N: int, S: str) -> bool:
    S = "0" + S

    if S[-1] == "1":
        return False

    dfs = [0]
    next_nodes = [2 ** i for i in range(N)]
    visited = [0] * (2 ** N)
    visited[0] = 0
    # print(next_nodes)

    while len(dfs) > 0:
        now = dfs.pop()

        if now == 2 ** N - 1:
            return True

        for next_put in next_nodes:
            if now | next_put == now:
                continue

            next_node = now | next_put

            if visited[next_node]:
                continue

            if S[next_node] == "1":
                continue
            visited[next_node] = 1
            dfs.append(next_node)

    return False



T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print("Yes" if solve(N, S) else "No")
