from itertools import permutations


N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
points = [{} for _ in range(N)]

for _ in range(M):
    a, b, c = [int(x) for x in input().split()]
    a -= 1
    b -= 1


    sides[a].append(b)
    points[a][b] = c

    sides[b].append(a)
    points[b][a] = c

sides_set = [set(x) for x in sides]

ans = -1
for route in permutations(range(N), N):
    now_ans = 0
    for i in range(N - 1):
        if route[i + 1] not in sides_set[route[i]]:
            break

        now_ans += points[route[i]][route[i + 1]]

    ans = max(ans, now_ans)

print(ans)
