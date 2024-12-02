# 解説AC。ポケポケ楽しいね！！
# とにかくdpを思いつけるかということ。本番ではにぶたんしてた人だけど()
# 制約が N,X < 5000 だったのが怪しかった。こういう時はdpを疑うべき！！

N, X = [int(x) for x in input().split()]
P = [int(x) / 100 for x in input().split()]

# 確率計算のDP！反復試行（各試行の確率が違う）をDPで計算できる。
# 縦：何枚目まで引いたか、横：当たりが何枚出たか
# これは本番でもできるようにしたい。
dp_prob = [[0] * (N + 1) for _ in range(N)]
dp_prob[0][0] = 1 - P[0]
dp_prob[0][1] = P[0]

for i in range(1, N):
    for j in range(N + 1):
        # 今回当たりだった場合は前回の数-1の確率から、外れだった場合は前回の数と同じ確率から
        dp_prob[i][j] = dp_prob[i - 1][j - 1] * P[i] + dp_prob[i - 1][j] * (1 - P[i])


# 期待値計算のDP！これは解説を見ないとわからなかった。
# 当たりがX枚以上出るときの、開けるパック数の期待値を計算していく。
# しかし0枚の時は今求めているdpの値が必要になってしまうので、式変形してうまいことやる。（これは分からん…。）
dp_expection = [0] * (X + 1)
dp_expection[0] = 0

for i in range(1, X + 1):
    exp = 1

    # 次のパックで（ここで+1）当たりをX枚引く確率に応じて、同じリスト内の「～枚以上出る期待値」をかけて足していく。
    for j in range(1, min(i, N) + 1):
        exp += dp_expection[i - j] * dp_prob[-1][j]

    # 0枚だった時の処理（上までで、1枚以上当たって目標を達成するときの期待値が出るのかな？）
    dp_expection[i] = exp / (1 - dp_prob[-1][0])

print(dp_expection[-1])
