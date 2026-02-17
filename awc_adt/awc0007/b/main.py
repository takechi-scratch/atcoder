N, K = [int(x) for x in input().split()]
research = []
for _ in range(N):
    input()
    research.append(set(input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if len(research[i] & research[j]) >= K:
            ans += 1

print(ans)
