N = int(input())
ans = 10 ** 18
for _ in range(N):
    A, P, X = [int(x) for x in input().split()]
    if A < X:
        ans = min(ans, P)

print(ans if ans < 10 ** 18 else -1)
