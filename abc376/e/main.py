from itertools import combinations
from sys import stdin
input = stdin.readline

def solve():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 10 ** 20
    for comb in combinations(range(N), K):
        a_sitei, b_sum = [], 0
        for i in comb:
            a_sitei.append(A[i])
            b_sum += B[i]

        ans = min(ans, max(a_sitei) * b_sum)

    return ans


T = int(input())
last_ans = []
for _ in range(T):
    last_ans.append(solve())

print("\n".join(map(str, last_ans)))
