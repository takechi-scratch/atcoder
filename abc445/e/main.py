MOD = 998244353

# あとで戻す！！！
max_A = 10**7 + 5
min_factor = [0] * max_A
for factor in range(2, max_A):
    for i in range(factor, max_A, factor):
        if min_factor[i] == 0:
            min_factor[i] = factor


def solve(N: int, A: list[int]):
    factors = {}

    for x in A:
        now = x
        while now > 1:
            now_factor = min_factor[now]
            count = 0
            while now % now_factor == 0:
                count += 1
                now //= now_factor

            if now_factor not in factors:
                factors[now_factor] = (count, 0)
            elif factors[now_factor][0] <= count:
                factors[now_factor] = (count, factors[now_factor][0])
            elif factors[now_factor][1] <= count:
                factors[now_factor] = (factors[now_factor][0], count)

    mul = 1
    for key, value in factors.items():
        mul *= pow(key, value[0], MOD)
        mul %= MOD

    ans = []
    for x in A:
        now_dist = 1
        now = x
        while now > 1:
            now_factor = min_factor[now]
            count = 0
            while now % now_factor == 0:
                count += 1
                now //= now_factor

            if factors[now_factor][0] == count:
                now_dist *= pow(now_factor, factors[now_factor][0] - factors[now_factor][1], MOD)
                now_dist %= MOD

        ans.append(mul * pow(now_dist, MOD - 2, MOD) % MOD)

    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print(" ".join([str(x) for x in solve(N, A)]))
