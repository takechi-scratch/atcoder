# https://atcoder.jp/contests/abc287/tasks/abc287_c
N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)] # 辺

for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

if N - M != 1:
    print("No")
    exit()

edge = []
for i in range(N):
    if len(sides[i]) > 2 or len(sides[i]) <= 0:
        print("No")
        exit()

    if len(sides[i]) == 1:
        edge.append(i)

if len(edge) != 2:
    print("No")
    exit()

visited = [False] * N
now = edge[0]
prev = -1
visited[now] = True
for _ in range(N - 1):
    if sides[now][0] != prev:
        next = sides[now][0]
    elif len(sides[now]) == 1:
        print("No")
        exit()
    else:
        next = sides[now][1]

    if visited[next] is True:
        print("No")
        exit()

    prev = now
    now = next
    visited[now] = True

if now == edge[1]:
    print("Yes")
else:
    print("No")
