from atcoder.dsu import DSU

N, Q = [int(x) for x in input().split()]
uf = DSU(N)
ufc = DSU(N)

sides = [[] for _ in range(N)]


def calc_max(x):
    return x // 2


ans = 0
for counter in range(Q):
    x, y = [int(x) - 1 for x in input().split()]
    sides[x].append(y)
    sides[y].append(x)
    if ufc.same(x, y):
        print(*[-1] * (Q - counter), sep="\n")
        exit()

    if not uf.same(x, y):
        ans -= calc_max(uf.size(x))
        ans -= calc_max(uf.size(y))
        ans += calc_max(uf.size(x) + uf.size(y))

    uf.merge(x, y)

    if len(sides[x]) > 0:
        same_color_merge = sides[x][0]
        ufc.merge(y, same_color_merge)

    if len(sides[y]) > 0:
        same_color_merge = sides[y][0]
        ufc.merge(x, same_color_merge)

    print(ans)
