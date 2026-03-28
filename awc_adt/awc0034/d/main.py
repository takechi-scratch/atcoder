from collections import defaultdict

N = int(input())
reservations = [[int(x) for x in input().split()] for _ in range(N)]
nodes = defaultdict(list)
nodes[0] = []
nodes[10**9] = []
for l, r in reservations:
    nodes[l] = nodes[l]
    nodes[r].append(l)

dp = defaultdict()
before = -1
for t in sorted(nodes.keys()):
    if t == 0:
        dp[t] = 0
        before = 0
        continue

    now_ans = dp[before]
    for l in nodes[t]:
        now_ans = max(now_ans, dp[l] + 1)

    dp[t] = now_ans
    before = t

print(dp[10**9])
