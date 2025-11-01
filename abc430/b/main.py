N, M = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(N)]

types = set()
for si in range(N - M + 1):
    for sj in range(N - M + 1):
        types.add(tuple(tuple(x[sj : sj + M]) for x in grid[si : si + M]))

print(len(types))
