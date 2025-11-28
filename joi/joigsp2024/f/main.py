# 漸化式を考えつつDPを立てる。
# 「計算量的にこれ」って考えるのと組み合わせながら。
# リストO(M), 1回の遷移当たりO(N)ってのはよくありそう。

N, M = [int(x) for x in input().split()]
chocolates = [[int(x) for x in input().split()] for _ in range(N)]

dp = []
for now_ticket in range(M + 1):
    ans = 0
    for a, b in chocolates:
        if now_ticket < a:
            continue

        ans = max(ans, b + dp[now_ticket - (a - b)])

    dp.append(ans)

dp = [x + i for i, x in enumerate(dp)]
first = 0
for need in range(1, M + 1):
    while dp[first] < need:
        first += 1
    print(int(first))
