N, K = [int(x) for x in input().split()]
print(*[int(x) // K for x in input().split() if int(x) % K == 0])
