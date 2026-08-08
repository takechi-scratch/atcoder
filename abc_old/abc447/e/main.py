from atcoder.dsu import DSU

N, M = [int(x) for x in input().split()]
merge_sides = [[int(x) - 1 for x in input().split()] for _ in range(M)]
uf = DSU(N)

merged = []
now_connected = 0
for u, v in reversed(merge_sides):
    if uf.leader(u) != uf.leader(v):
        if now_connected == N - 2:
            merged.append(False)
            continue
        now_connected += 1
    uf.merge(u, v)
    merged.append(True)

ans = 0
MOD = 998244353
for i in range(M):
    if not merged[M - i - 1]:
        ans += pow(2, i + 1, MOD)
        ans %= MOD

print(ans)
