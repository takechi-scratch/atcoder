N, M = [int(x) for x in input().split()]
people_votes = [list(input()) for _ in range(N)]
votes = [[people_votes[j][i] for j in range(N)] for i in range(M)]
points = [0] * N

for x in votes:
    if x.count("1") > x.count("0"):
        minority = "0"
    else:
        minority = "1"

    for i in range(N):
        points[i] += (x[i] == minority)

win = max(points)
ans = [i + 1 for i in range(N) if points[i] == win]
print(*ans)
