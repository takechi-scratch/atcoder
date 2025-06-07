from math import lcm

N, M, K = [int(x) for x in input().split()]
NM_LCM = lcm(N, M)

# ans以下の条件を満たす数の個数
def counts(ans):
    return ans // N + ans // M - ans // NM_LCM * 2

# ansを決め打ちにぶたん
# 個数がK個となる最小のansを求めれば、それが答え
under, over = 0, 10 ** 18
while over - under > 1:
    test_ans = (under + over) // 2
    if counts(test_ans) > K:
        over = test_ans
    else:
        under = test_ans

print(over)
