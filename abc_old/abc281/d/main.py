from collections import defaultdict, Counter

N, K, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

D_factorizated = Counter(D)
dp = [[defaultdict(lambda: -1) for _ in range(K)] for _ in range(N)]
