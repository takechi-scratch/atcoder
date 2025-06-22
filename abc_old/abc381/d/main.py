N = int(input())
A = [int(x) for x in input().split()]

ans = 0

def solve(A):
    global ans

    nums = set()
    left, right = -1, -1
    for i in range(0, N, 2):
        ans = max(ans, right - left)

        if i + 1 >= len(A):
            continue

        if A[i] != A[i + 1]:
            left, right = i + 1, i + 1
            # WAポイント！条件を満たさなくなった際の初期化を欠かさない。
            nums = set()
            continue

        while len(nums) > 0 and A[i] in nums:
            left += 2
            nums.remove(A[left])

        nums.add(A[i])
        right = i + 1
        ans = max(ans, right - left)

solve(A)
solve([-1] + A)

print(ans)
