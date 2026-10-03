N, V = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if i + j + k + 3 > V:
                continue

            ans = max(ans, W[i] + W[j] + W[k])

print(ans)
