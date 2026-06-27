from sortedcontainers import SortedSet

N, M, S = [int(x) for x in input().split()]
ss = SortedSet(range(N))
now_idx = S - 1

for _ in range(M):
    ss.pop(now_idx)
    d = int(input())
    now_idx = (now_idx + d - 1) % len(ss)

print(ss[now_idx] + 1)
