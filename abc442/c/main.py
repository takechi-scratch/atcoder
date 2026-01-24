N, M = [int(x) for x in input().split()]
ng = [[i] for i in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    ng[a].append(b)
    ng[b].append(a)

ans = []
for i in range(N):
    person_count = N - len(ng[i])
    ans.append(person_count * (person_count - 1) * (person_count - 2) // 6)

print(*ans)
