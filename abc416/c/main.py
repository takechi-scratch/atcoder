from itertools import product

N, K, X = [int(x) for x in input().split()]
S = [input() for _ in range(N)]

concats = ["".join(s) for s in product(S, repeat=K)]
concats.sort()
# print(concats)
print(concats[X - 1])
