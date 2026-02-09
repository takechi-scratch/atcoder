N, K = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

D.sort()
print(sum(D[: N - K]))
