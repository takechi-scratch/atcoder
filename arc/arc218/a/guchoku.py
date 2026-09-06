from itertools import product

N, M = [int(x) for x in input().split()]
A = [[int(x) - 1 for x in input().split()] for _ in range(N)]
MOD = 998244353

ans = 0
for nums in product(*A):
    ans += len(set(nums))

print(ans)
