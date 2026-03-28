from collections import defaultdict

N, M = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
T = [int(input()) - 1 for _ in range(M)]

d = defaultdict(int)
for x in T:
    d[x] += 1

print(sum(min(d[i], C[i]) for i in range(N)))
