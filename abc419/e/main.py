N, M, L = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

groups = [[] for _ in range(L)]
for i, x in enumerate(A):
    groups[i % L].append(x)

# ここ全体の計算量は、3重ループに見えて実はO(MN)
mod_group_min = [[-1] * L for _ in range(M)]
for mod in range(M):
    # この内部で、xは合計でN個分しか作られないから
    for j in range(L):
        need_steps = 0
        for x in groups[j]:
            need_steps += (mod - x) % M

        mod_group_min[mod][j] = need_steps

dp = [[10 ** 18] * M for _ in range(L + 1)]
dp[0][0] = 0
for i in range(1, L + 1):
    for now_mod in range(M):
        now_ans = 10 ** 18
        for before_mod in range(M):
            now_ans = min(now_ans, dp[i - 1][before_mod] + mod_group_min[(now_mod - before_mod) % M][i - 1])

        dp[i][now_mod] = now_ans

print(dp[-1][0])
