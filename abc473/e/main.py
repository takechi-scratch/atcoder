N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A_sum = [0]
for x in A:
    A_sum.append((A_sum[-1] + x) % K)

ans = 0
waiting_nums = {0}
for right in range(1, N + 1):
    if A_sum[right] in waiting_nums:
        ans += 1
        waiting_nums = set()
    waiting_nums.add(A_sum[right])

print(ans)
