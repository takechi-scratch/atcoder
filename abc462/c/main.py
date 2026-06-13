N = int(input())
points = [[int(x) for x in input().split()] for _ in range(N)]
x_points = [None] * N
for x, y in points:
    x_points[y - 1] = x

ans = 0
min_x = 10**18
for y, x in enumerate(x_points, start=1):
    if not min_x < x:
        ans += 1
    min_x = min(min_x, x)

print(ans)
