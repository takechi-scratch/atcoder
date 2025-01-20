# WA・TLE解答。
from itertools import combinations, permutations

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

before_picks = tuple(range(K))

ans = 0
for i in before_picks:
    ans = ans ^ A[i]
before_ans = ans

for picks in permutations(range(N), K):
    temp_ans = before_ans
    # 前回との差を計算する的な感じ
    for i in range(K - 1, -1, -1):
        if before_picks[i] != picks[i]:
            temp_ans = temp_ans ^ A[before_picks[i]] ^ A[picks[i]]
        else:
            break
    before_ans = ans
    before_picks = picks
    ans = max(ans, temp_ans)


print(ans)
