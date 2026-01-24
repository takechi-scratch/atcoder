from itertools import product

N = int(input())
L = [int(x) for x in input().split()]
sides_raw = [[int(x) - 1 for x in input().split()] for _ in range(N - 1)]

if N > 7:
    exit()

for status in product(range(4), repeat=N-1):
    now_sides = [[] for _ in range(N)]
    for i, x in enumerate(sides_raw):
        if status[i] == 0:
            now_sides[x[0]].append(x[1])
            now_sides[x[1]].append(x[0])
        elif status[i] == 1:
            now_sides[x[0]].append(x[1])
        elif status[i] == 2:
            now_sides[x[1]].append(x[0])

    now_l = [0] * N
    for start in range(N):
        visited = [False] * N
        visited[start] = True
        dfs = [start]
        while len(dfs) > 0:
            now = dfs.pop()
            for next_node in now_sides[now]:
                if visited[next_node]:
                    continue
                dfs.append(next_node)
                visited[next_node] = True

        now_l = [x + int(visited[i]) for i, x in enumerate(now_l)]

    if all(x == y for x, y in zip(L, now_l)):
        print("YES")
        break

else:
    print("NO")
