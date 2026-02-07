N, M = [int(x) for x in input().split()]
birds = [[int(x) for x in input().split()] for _ in range(N)]
reports = [[0, 0] for _ in range(M)]

for a, b in birds:
    reports[a - 1][0] += 1
    reports[a - 1][1] += b

print(*[f"{x[1] / x[0]:.10f}" for x in reports], sep="\n")
