N, K = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]

# サイコロそれぞれについて考えて、合計する
exp = [(p + 1) / 2 for p in P]

# 累積和を使えば合計が分かる
exp_sum = [0]
for x in exp:
    exp_sum.append(exp_sum[-1] + x)

ans = 0
for i in range(K, N + 1):
    ans = max(ans, exp_sum[i] - exp_sum[i - K])

print(ans)
