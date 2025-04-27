N, K = [int(x) for x in input().split()]
S = [input() for _ in range(N)][:K]
S.sort()
print(*S, sep="\n")
