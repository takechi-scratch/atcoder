# 個数をカウントし、modDで分ける。
# そうすると、隣接しない中でできるだけ多く数字をとればいい...DP
# 数が隣接しない部分はDPを変えないといけない！！

N, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

if D == 0:
    print(len(A) - len(set(A)))
    exit()

A_dict = {}
for i in range(N):
    if A[i] not in A_dict:
        A_dict[A[i]] = 0
    A_dict[A[i]] += 1

mod_divides = [dict() for _ in range(D)]

for i in A_dict.keys():
    if i // D not in mod_divides[i % D]:
        mod_divides[i % D][i // D] = 0
    mod_divides[i % D][i // D] += A_dict[i]

ans = 0
for div in mod_divides:
    dp = [0, 0]
    before = -10000
    for i in sorted(div.keys()):
        if i - before == 1:
            dp = [dp[1], min(dp[0], dp[1]) + div[i]]
        else:
            dp = [min(dp[0], dp[1]), min(dp[0], dp[1]) + div[i]]

        before = i

    ans += min(dp)

print(ans)
