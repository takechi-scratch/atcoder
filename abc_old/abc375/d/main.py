"""
累積和っぽい問題。
これは解説(2)でやった方法に近いかな。

はさむ数を固定してみたとき、間にある文字の数が回文の数と等しい。
そのため、XYYXYYX のとき、2番目のXが出現した段階で1→2の場合の数、
3番目のXが出現した段階で1→3と2→3の場合の数を足す。
つまり累積和。（？）

実装としては、hueruをcounterずつ増やし、出現したらポイントに足す。
"""

S = list(input())
strlist = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

counter = [0] * 26
hueru = [0] * 26
sum_point = [0] * 26

for i, mozi in enumerate(S):
    str_index = strlist.index(mozi)

    sum_point[str_index] += hueru[str_index]

    hueru = [hueru[x] + counter[x] for x in range(26)]

    counter[str_index] += 1

print(sum(sum_point))
