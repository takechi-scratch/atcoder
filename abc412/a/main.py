N = int(input())
ans = 0
for _ in range(N):
    A, B = [int(x) for x in input().split()]
    if A < B:
        ans += 1

print(ans)
