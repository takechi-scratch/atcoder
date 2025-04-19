N, M = [int(x) for x in input().split()]
sides_count = [0] * N
for _ in range(M):
    a, b = [int(x) for x in input().split()]
    sides_count[(a + b) % N] += 1

ans = M * (M - 1) // 2
for x in sides_count:
    ans -= x * (x - 1) // 2

print(ans)
