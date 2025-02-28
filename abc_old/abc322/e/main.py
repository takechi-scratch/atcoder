# 解説AC。
# パラメータの場合数が少ないことは分かっていたので、
# 「どこを取るか」をDPに付けて順番に試せばよかった！！

N, K, P = [int(x) for x in input().split()]
get_points = []
costs = []
for _ in range(N):
    n = [int(x) for x in input().split()]
    get_points.append(n[1:])
    costs.append(n[0])

if not all([sum([get_points[j][i] for j in range(N)]) >= P for i in range(K)]):
    print(-1)
    exit()

dp: list[int] = [10 ** 18] * ((P + 1) ** K)
dp[0] = 0

for i in range(N):
    next_dp = dp.copy()
    for bits_raw in range((P + 1) ** K):
        if dp[bits_raw] >= 10 ** 18:
            continue

        temp = bits_raw
        bits = []
        for j in range(K - 1, -1, -1):
            bits.append(temp // ((P + 1) ** j))
            temp %= (P + 1) ** j

        for j, x in enumerate(bits):
            bits[j] = min(P, x + get_points[i][j])

        next_bit = int("".join([str(x) for x in bits]), P + 1)
        if dp[bits_raw] + costs[i] <= dp[next_bit]:
            next_dp[next_bit] = dp[bits_raw] + costs[i]

    dp = next_dp.copy()

print(dp[-1])
