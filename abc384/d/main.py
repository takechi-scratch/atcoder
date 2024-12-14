N, S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# Aの合計で割った分は、A全体を何回か繰り返せばOK
# 余りの部分を考える
S %= sum(A)
# 後ろと前がつながってるので2周しておく
tansaku = A * 2

# しゃくとりっぽいことをしてみた
score = 0
left, right = 0, 0
moved = True

# WAポイント！whileの条件に注意
# 「真の間」繰り返す。TrueとFalse, andとorに注意
while moved is True:
    moved = False
    if score == S:
        print("Yes")
        break

    # スコアが足りない間は右を動かす
    while score < S and right < len(tansaku):
        right += 1
        score += tansaku[right - 1]
        moved = True

    # スコアが多い間は左を動かす
    while score > S and left < len(tansaku):
        left += 1
        score -= tansaku[left - 1]
        moved = True

else:
    print("No")
