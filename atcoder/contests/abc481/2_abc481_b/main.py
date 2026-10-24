N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = A[0] == K
for i in range(N - 1):
    if A[i] != K and min(A[i], A[i + 1]) <= K <= max(A[i], A[i + 1]):
        ans += 1

print(int(ans))
