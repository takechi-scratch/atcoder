from math import isqrt
MOD = 998244353

N = int(input())

def gausu_sum(N: int, MOD: int = 998244353):
    """ガウス記号の分数 [N / k] をk=1...Nまで動かした総和。
       計算回数は2 * (N ** 1/2)回程度で、N=10**12くらいまでは行ける"""

    ans = 0

    for x in range(1, isqrt(N) + 1):
        ans += N // x
        ans %= MOD

    now_end = N
    for x in range(1, isqrt(N) + 1):
        # 最大でもisqrt(N)に押さえつけることで、境界での数え間違いを防止
        next_end = max(N // (x + 1), isqrt(N))
        ans += x * (now_end - next_end)
        ans %= MOD
        now_end = next_end

    return ans

ans = 0
ans += N % MOD * (N - 2) % MOD
ans -= (N + 1) % MOD * ((N - 2) % MOD) * pow(2, -1, MOD)
ans += N - 2
ans %= MOD

ans -= gausu_sum(N) - (N + 1)
ans %= MOD

gausu_sum(100)

print(ans)
