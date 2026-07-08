from itertools import combinations
from functools import lru_cache

MOD = 998244353

N = int(input())
N_MOD = N % MOD
N_nums = list(str(N))
M = len(N_nums)


@lru_cache(maxsize=None)
def calc_ans(i: int, max_x: int, mod3: int, nums: tuple[int], must_nums: tuple[int]):
    # numsのみを使う
    if i == M - 1:
        ans = 0
        for x in nums:
            ans += int(x <= max_x and x % 3 == mod3 and len(must_nums) == 0)
        return ans

    ans = 0
    for x in nums:
        if i == 0 and x == 0:
            continue

        if x < max_x:
            ans += calc_ans(i + 1, 10, (mod3 - i) % 3, nums, tuple(y for y in must_nums if y != x))

        elif x == max_x:
            ans += calc_ans(i + 1, int(N_nums[i + 1]), (mod3 - x) % 3, nums, tuple(y for y in must_nums if y != x))

        ans %= MOD

    return ans % MOD


@lru_cache(maxsize=None)
def calc_ans2(i: int, max_x: int, mod3: int):
    # 十進表記に3を含まないもの
    if i == M:
        return int(mod3 == 0)

    ans = 0
    for x in range(max_x):
        if i == 0 and x == 0:
            continue

        if x == 3:
            continue

        ans += calc_ans2(i + 1, 10, (mod3 - i) % 3)
        ans %= MOD

    if max_x < 10:
        ans += calc_ans2(i + 1, int(N_nums[i + 1] if i + 1 < M else 10), (mod3 - max_x) % 3)

    return ans % MOD


# A: (not 1) and 2 - B: (not 1) and 2 and 3
# C: 1 and (not 2) - D: 1 and (not 2) and 3

# A: (not 1) - (not 1) and (not 2)

ans = 0
for nums in combinations([0, 1, 2, 4, 5, 6, 7, 8, 9], 3):
    # (not 1) and (not 2) and 3
    ans += calc_ans(0, int(N_nums[0]), 1, nums, nums)
    ans += calc_ans(0, int(N_nums[0]), 2, nums, nums)

    ans -= calc_ans(0, int(N_nums[0]), 0, nums, nums)  # D


for nums_a in combinations([0, 1, 2, 4, 5, 6, 7, 8, 9], 2):
    nums = list(nums_a)
    nums.append(3)
    nums = tuple(sorted(nums))

    # B
    ans += calc_ans(0, int(N_nums[0]), 1, nums, nums)
    ans += calc_ans(0, int(N_nums[0]), 2, nums, nums)


ans -= calc_ans2(0, int(N_nums[0]), 1)
ans -= calc_ans2(0, int(N_nums[0]), 2)
ans += calc_ans2(0, int(N_nums[0]), 0)

ans += N_MOD - (N // 3) % MOD
ans %= MOD
print(ans)
