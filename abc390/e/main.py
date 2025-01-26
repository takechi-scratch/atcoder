# 解説AC。
# 問題文的にナップザック問題、DPを使う。
# 各食べ物にはビタミンが1種類しか含まれていないのがミソ！！
# 各ビタミンごとにカロリーを割り当てて、その中でのビタミンの最大値をすぐに求められる

N, X = [int(x) for x in input().split()]
food = []
for _ in range(N):
    food.append([int(x) for x in input().split()])

dp = [[0] * (X + 1) for _ in range(3)]

for i in range(N):
    v, a, c = food[i]
    v -= 1

    # Nが0～Nまでの全てを保持する必要はない！
    # next_dpを新しく定義し、置換していく形で
    next_dp = [0] * (X + 1)
    for j in range(X + 1):
        next_dp[j] = dp[v][j]
        if j - c >= 0:
            next_dp[j] = max(next_dp[j], dp[v][j - c] + a)

        if j >= 1:
            next_dp[j] = max(next_dp[j], next_dp[j - 1])

    dp[v] = next_dp

# 解説と同じ解法。1カロリーずつ増やしていく中で、一番足りないビタミンへの割り当てを増やし、
# DPからその時の最大ビタミンを求める。
cal = [0] * 3
vitamin = [0] * 3
for i in range(X):
    min_vitamin = vitamin.index(min(vitamin))

    cal[min_vitamin] += 1
    vitamin[min_vitamin] = dp[min_vitamin][cal[min_vitamin]]

print(min(vitamin))
