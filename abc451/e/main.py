N = int(input())
dists = [[int(x) for x in input().split()] for _ in range(N - 1)]


def get_dist(a: int, b: int):
    if a == b:
        return 0
    if a > b:
        a, b = b, a
    return dists[a][b - a - 1]


nearest_points = [10**18] + dists[0][:]
connected = {0}

for _ in range(N - 1):
    nearest_node = nearest_points.index(min(nearest_points))
    connect_node = min(range(N), key=lambda x: get_dist(nearest_node, x) if x != nearest_node else 10**18)

    for test in connected:
        if get_dist(nearest_node, test) > get_dist(nearest_node, connect_node) + get_dist(connect_node, test):
            print("No")
            exit()

    nearest_points[nearest_node] = 10**18
    for x in range(N):
        if nearest_points[x] == 10**18:
            continue
        nearest_points[x] = min(nearest_points[x], get_dist(x, nearest_node))

    connected.add(nearest_node)

print("Yes")
