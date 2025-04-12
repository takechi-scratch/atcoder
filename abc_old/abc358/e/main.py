K = int(input())
C = [int(x) for x in input().split()]
MOD = 998244353

dp = [[1] * C[i] for i in range(26)]

for i in range(K):
    next_dp = [[-1] * C[i] for i in range(26)]
    for char in range(26):
        for now in range(C[char]):
            next_pattern = 0
            for before_char in range(26):
                if char == before_char:
                    if now == 0 or C[before_char] == 0:
                        continue
                    next_pattern += dp[before_char][-2] % MOD
                else:
                    if C[before_char] == 0:
                        continue
                    next_pattern += dp[before_char][-1] % MOD

            next_dp[char][now] = next_pattern % MOD

    dp = next_dp

print(dp[0][-1])
