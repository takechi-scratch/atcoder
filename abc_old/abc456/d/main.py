# ほんとはdp

S = list(input())
N = len(S)
MOD = 998244353

ans = 0
now_sum = [0, 0, 0]
for i, x in enumerate(S):
    x_id = "abc".index(x)
    now_ans = sum(now_sum) - now_sum[x_id]
    now_ans += 1
    ans += now_ans
    ans %= MOD
    now_sum[x_id] += now_ans
    now_sum[x_id] %= MOD

print(ans)
