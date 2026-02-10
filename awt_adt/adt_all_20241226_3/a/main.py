# https://atcoder.jp/contests/abc332/tasks/abc332_a
N, S, K = [int(x) for x in input().split()]
ans = 0

for _ in range(N):
    p, q = [int(x) for x in input().split()]
    ans += p * q

if ans < S:
    ans += K

print(ans)
