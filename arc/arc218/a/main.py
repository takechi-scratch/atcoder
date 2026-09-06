N, M = [int(x) for x in input().split()]
A = [[int(x) - 1 for x in input().split()] for _ in range(N)]
MOD = 998244353

mod_pow = [1]
for _ in range(600):
    mod_pow.append((mod_pow[-1] * M) % MOD)

ans = 0
used_pattern = [0] * (N * M)
for i, x in enumerate(A):
    ans *= M
    ans %= MOD
    for j in range(M):
        ans += mod_pow[i] - used_pattern[x[j]]
        ans %= MOD

    num_counter = {}
    for y in x:
        num_counter[y] = num_counter[y] + 1 if y in num_counter else 1

    for num in range(N * M):
        num_appeared = num_counter[num] if num in num_counter else 0
        before_pattern = used_pattern[num]
        used_pattern[num] = before_pattern * (M - num_appeared) + num_appeared * mod_pow[i]
        used_pattern[num] %= MOD

print(ans)
