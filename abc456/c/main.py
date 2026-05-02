from bisect import bisect_left

S = list(input())
N = len(S)
MOD = 998244353

next_ng = [i for i in range(N - 1) if S[i] == S[i + 1]] + [N - 1]

ng_count = 0
for start in range(N):
    ng_count += N - next_ng[bisect_left(next_ng, start)] - 1

print(((N + 1) * N // 2 - ng_count) % MOD)
