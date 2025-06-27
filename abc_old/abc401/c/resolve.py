N, K = [int(x) for x in input().split()]

MOD = 10 ** 9
nums = [1] * K
now_sum = K

for i in range(K, N + 1):
    nums.append(now_sum % MOD)

    now_sum += now_sum
    now_sum -= nums[i - K]
    now_sum %= MOD

print(nums[-1])
