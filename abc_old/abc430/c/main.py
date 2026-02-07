# 複雑な条件→「かつ」とか「または」を使って簡単にできないか考える。（包除原理）

from bisect import bisect_left

N, A, B = [int(x) for x in input().split()]
S = list(input())
A_sum = [0]
B_sum = [0]
for x in S:
    A_sum.append(A_sum[-1] + (x == "a"))
    B_sum.append(B_sum[-1] + (x == "b"))

ans_b = 0
for left in range(N):
    ans_b += N - bisect_left(B_sum, B_sum[left] + B)

ans_or = 0
for left in range(N):
    ans_or += N - min(bisect_left(A_sum, A_sum[left] + A), bisect_left(B_sum, B_sum[left] + B))

print(ans_or - ans_b)
