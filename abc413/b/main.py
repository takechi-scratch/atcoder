N = int(input())
S = [input() for _ in range(N)]

ans = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans.add(S[i] + S[j])

print(len(ans))
