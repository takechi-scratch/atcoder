def query(c):
    print("?", len(c), *c)
    return [tuple(map(int, input().split())) for _ in range(len(c) - 1)]


def answer(groups, edges):
    print("!")
    for i in range(len(groups)):
        print(*groups[i])
        for e in edges[i]:
            print(*e)


# read input
N, M, Q, L, W = map(int, input().split())
G = list(map(int, input().split()))
lx, rx, ly, ry = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    lx.append(a)
    rx.append(b)
    ly.append(c)
    ry.append(d)

# use center of rectangle
x = [(l + r) // 2 for l, r in zip(lx, rx)]
y = [(l + r) // 2 for l, r in zip(ly, ry)]

# split cities into groups
cities = list(range(N))
cities.sort(key=lambda i: (x[i], y[i]))
groups = []
start_idx = 0
for g in G:
    groups.append(cities[start_idx : start_idx + g])
    start_idx += g

# get edges from queries
edges = []
for k in range(M):
    edges.append([])
    for i in range(0, G[k] - 1, 2):
        if i < G[k] - 2:
            ret = query(groups[k][i : i + 3])
            edges[k].extend(ret)
        else:
            edges[k].append(groups[k][i : i + 2])

# output answer
answer(groups, edges)

