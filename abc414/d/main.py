N, M = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
X.sort()

dists = [X[i + 1] - X[i] for i in range(N - 1)]
dists.sort()

print(sum(dists[:N - M]))
